#!/bin/bash

#create RDS Instance
#aws rds create-db-instance --db-instance-class db.t2.micro --allocated-storage 30 --db-instance-identifier my-cool-rds-db --engine mysql --master-username masteruser --master-user-password masterpassword1! --profile royalenter

#modify instance - maintenance-window
#aws rds modify-db-instance --db-instance-identifier my-cool-rds-db --preferred-maintenance-window Mon:07:00:00-Mon:07:30 --profile royalenter

#modify instance - vertical scalling
#aws rds modify-db-instance --db-instance-identifier my-cool-rds-db --db-class db.t2.medium --profile royalenter

#generate auth-token
#aws rds generate-db-auth-token --hostname my-cool-rds-db.cw5emdaynoxo.us-east-1.rds.amazonaws.com --port 3306 --username eestevez-royalenter --profile royalenter

RDSHOST="my-cool-rds-db.cw5emdaynoxo.us-east-1.rds.amazonaws.com"
TOKEN="$(aws rds generate-db-auth-token --hostname $RDSHOST --port 3306 --region us-east-1 --username masteruser --profile royalenter )"
mysql --host=$RDSHOST --port=3306 --ssl-ca=rds-combined-ca-bundle.pem --user=masteruser --password=$TOKEN

#echo $TOKEN;

eestevez-royalenter
vAJ*rn^y[t+<5r8b

&MgVrA3#

