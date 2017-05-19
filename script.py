#!/usr/bin/env python3

import boto3
import time

s3 = boto3.resource('s3')
cronFile = open('/var/log/cron','rb')
s3.Bucket('stephenkwansbucket').put_object(Key='cron', Body=cronFile)

