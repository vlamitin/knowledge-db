#!/bin/bash
# restic wrapper
echo "enter restic connection string:"; read -s IN; \

export RESTIC_REPOSITORY=$(echo $IN | awk -F '@@@@@' '{print $1}'); \
export AWS_ACCESS_KEY_ID=$(echo $IN | awk -F '@@@@@' '{print $2}'); \
export AWS_SECRET_ACCESS_KEY=$(echo $IN | awk -F '@@@@@' '{print $3}'); \
export RESTIC_PASSWORD=$(echo $IN | awk -F '@@@@@' '{print $4}')
