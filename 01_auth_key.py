#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' generate a 20 length random key for activating'

__author__ = 'fishzd'


import random
import mysql.connector
import redis

#generate the keys


low_case = [chr(a) for a in range(97, 123)]
up_case = [chr(A) for A in range(65, 91)]
num = [chr(n) for n in range(48, 58)]
all_char = low_case + up_case + num
key_dict = {}
while len(key_dict) != 200:
    key = ''.join(random.sample(all_char, 20))
    key_dict[key] = 1
print(key_dict)


#save keys to mysql
conn = mysql.connector.connect(user='root', password='password', database='miniproject')
cursor = conn.cursor()
cursor.execute('drop table auth_keys')
cursor.execute('create table auth_keys (auth_key varchar(20) primary key, isValid boolean)')
for key, isValid in key_dict.items():
    cursor.execute('insert into auth_keys (auth_key, isValid) values (%s, %s)', [key, isValid])
print(cursor.rowcount)

conn.commit()
cursor.close()
conn.close()


r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.delete('auth_keys')
r.hmset('auth_keys', key_dict)