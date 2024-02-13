#!/bin/bash
# SSH 접속과 동시에 로봇의 시간을 동기화하는 스크립트

# 로봇의 사용자 이름과 호스트를 설정
ROBOT_USER="zeta"
ROBOT_HOST="10.42.0.1"

# 클라이언트의 현재 시간을 'YYYY-MM-DD HH:MM:SS' 형식으로 가져옵니다.
LOCAL_TIME=$(date +"%Y-%m-%d %H:%M:%S")

# SSH를 사용하여 로봇에 접속하고, 로봇의 시간을 설정하는 명령을 전송합니다.
ssh -t $ROBOT_USER@$ROBOT_HOST "sudo -S date -s '$LOCAL_TIME'"