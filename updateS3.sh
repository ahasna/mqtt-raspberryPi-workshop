#!bin/bash

cd session-2/dashboard
aws s3 cp . s3://mqtt-raspi --recursive 