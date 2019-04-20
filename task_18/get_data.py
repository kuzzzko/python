#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import sqlite3
import sys

def output_with_2args(key,value,keys,cursor_obj):
    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)
    for row in cursor_obj:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)

def output_with_0args(cursor_obj):
    print('\nВ таблице dhcp такие записи:')
    print('-' * 73)
    for row in cursor_obj:
        print('{:20}  {:15}  {:5}  {:18}  {}  {}'.format(*row))

db_filename = 'dhcp_snooping.db'
conn = sqlite3.connect(db_filename)

if len(sys.argv) == 3:
    key,value = sys.argv[1:]
    keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
    if key not in keys:
        print('Данный параметр не поддерживается.')
        print('Допустимые значения параметров: {}'.format(', '.join(keys)))
    else:
        keys.remove(key)
        conn.row_factory = sqlite3.Row
        query = 'select * from dhcp where {} = ?'.format(key)
        result = conn.execute(query, (value, ))
        output_with_2args(key,value,keys,result)
elif len(sys.argv) == 1:
    output_with_0args(conn.execute('select * from dhcp'))
else:
    print('Пожалуйста, введите два или ноль аргументов')


