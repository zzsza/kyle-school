FROM jupyter/minimal-notebook
RUN pip install tensorflow

RUN jupyter notebook --generate-config --allow-root -y  \
    && echo "c.NotebookApp.password = 'sha1:fee705da7ee3:39094efec15c2bc5f651b88fdd5536685b5fd229'" >> /home/jovyan/.jupyter/jupyter_notebook_config.py

EXPOSE 8888

ENTRYPOINT jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --no-browser 
