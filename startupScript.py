#!/usr/bin/env python3

import boto3
ec2 = boto3.resource('ec2')
userDataScript = """#!/bin/bash
sudo su
yum update -y
yum install python35 -y
yum install python35-pip -y
/usr/local/bin/pip3 install boto3"""
ec2.create_instances(ImageId='ami-c58c1dd3', 
                    MinCount=1, 
                    MaxCount=1,
                    KeyName='pythonProjectInstance'
                    user_data=userDataScript,
                    InstanceType='t2.micro')

