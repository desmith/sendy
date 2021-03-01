#!/usr/bin/env bash

source /home/ec2-user/rss2email/.venv/bin/activate

cd /home/ec2-user/rss2email

direnv allow . && eval "$(direnv export bash)"

./sendyrsspub.py send_newsletter
