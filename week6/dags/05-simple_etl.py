from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator

# 시나리오
# Google Cloud Storage에 매일 하루에 1번씩 주기적으로 csv 파일이 저장됨
# - csv 파일을 BigQuery에 Load
# - BigQuery에서 쿼리를 돌린 후, 일자별로 사용량 쿼리해서 Table 저장

default_args = {
    'owner': 'kyle',
    'depends_on_past': False,
    'start_date': datetime(2020, 2, 9),
    'email': ['your@mail.com'],
    'email_on_failure': False,
    'email_on_retry': True,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
    'end_date': datetime(2020, 2, 13),
    'project_id': 'my-project-1541645429744'
}

dag = DAG('simple_etl_storage_to_bigquery',
          default_args=default_args,
          schedule_interval='30 0 * * *')

execution_date = '{{ ds_nodash }}'


storage_to_bigquery_task = GoogleCloudStorageToBigQueryOperator(
    dag=dag,
    google_cloud_storage_conn_id='google_cloud_default',
    bigquery_conn_id='google_cloud_default',
    task_id='storage_to_bigquery',
    schema_object='data/bike_schema.json',
    bucket='kyle-school', # 생성한 bucket 이름을 넣으세요
    source_objects=[f"data/bike_data_{execution_date}.csv"],
    source_format='CSV',
    destination_project_dataset_table=f'my-project-1541645429744.temp.bike_{execution_date}', # 맨 앞 project_id 변경하세요
    write_disposition='WRITE_TRUNCATE',
    skip_leading_rows=1
)

agg_query = f"""
SELECT 
  dummy_date, start_station_id, end_station_id, COUNT(bikeid) as cnt
FROM `my-project-1541645429744.temp.bike_{execution_date}`
GROUP BY dummy_date, start_station_id, end_station_id
"""

query_task = BigQueryOperator(
        dag=dag,
        task_id="query_to_table",
        bigquery_conn_id='google_cloud_default',
        sql=agg_query,
        use_legacy_sql=False,
        destination_dataset_table=f"temp.bike_agg_{execution_date}"
)

storage_to_bigquery_task >> query_task
