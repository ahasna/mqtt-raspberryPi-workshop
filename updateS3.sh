#!bin/bash
cd code/dashboard
aws s3 cp . s3://mqtt-raspi --recursive