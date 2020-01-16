#!/bin/bash

set -euo pipefail
# 종료가 되거나 끝나면 메세지 전송
trap '[ "$?" -eq 0 ] || send_error ${LINENO} ${FUNCNAME}' EXIT

function send_error {
  local lineno=$1
  local funname=$2
  local current_date=$(date '+%Y-%m-%d %H:%M:%S')
  curl 'https://hooks.slack.com/services/T00000000/BXXXXX/asdasdasd' -d "payload={\"text\": \"[CRON][ERROR] LineNum=${lineno} FunName=${funname}\"}"
}

function slack_test {
   echo "now sleep..."
   echo "command + c"
   sleep 5
}