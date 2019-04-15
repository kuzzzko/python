#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import sqlite3
import sys
db_filename = 'dhcp_snooping.db'

def output_with_2args(key,value,keys,cursor_obj):
    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)
    for row in cursor_obj:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)

def output_with_0args(cursor_obj):
    print('\nВ таблице dhcp такие записи:')
    print('-' * 70)
    for row in cursor_obj:
        print('{:20}  {:15}  {:5}  {:18}  {}'.format(*row))

conn = sqlite3.connect(db_filename)

if len(sys.argv) == 3:
    key,value = sys.argv[1:]
    keys = ['mac', 'ip', 'vlan', 'interface']
    keys.remove(key)
    conn.row_factory = sqlite3.Row
    query = 'select * from dhcp where {} = ?'.format(key)
    result = conn.execute(query, (value, ))
    output_with_2args(key,value,keys,result)
elif len(sys.argv) == 1:
    result = conn.execute('select * from dhcp')
    output_with_0args(result)
else:
    print('Пожалуйста, введите два или ноль аргументов')


