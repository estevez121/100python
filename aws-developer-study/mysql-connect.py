# !/usr/bin/env python3.7
# -*- coding: utf-8 -*-

"""
Python Example to connect MySQL Database
"""

import pymysql

try:
    host = 'my-cool-rds-db.cw5emdaynoxo.us-east-1.rds.amazonaws.com'
    user = 'masteruser'
    password = 'masterpassword1!'
    db_name = 'db_test_1'

    conn = pymysql.connect(host, user=user, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur = conn.cursor()
        cur.execute("SELECT * FROM metadata")

        rows = cur.fetchall()
        for row in rows:
            print("{0} {1}".format(row[0], row[1]))

    conn.close()

except pymysql.MySQLError as e:
    print('MySQLError {}"'.format(e))
    raise e

