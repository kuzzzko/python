#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import sqlite3
import sys

def output_with_2args(keys,cursor_obj):
    for row in cursor_obj:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)

def output_with_0args(cursor_obj):
    for row in cursor_obj:
        print('{:20}  {:15}  {:5}  {:18}  {}'.format(*row))

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
        print('\nDetailed information for host(s) with', key, value)
        print('-' * 40)
        query_act = 'select * from dhcp where {} = ? and active = 1'.format(key)
        output_with_2args(keys,conn.execute(query_act, (value, )))
        print('\n' + '=' * 40)
        print('\nInactive values:')
        print('-' * 40)
        query_inact = 'select * from dhcp where {} = ? and active = 0'.format(key)
        output_with_2args(keys, conn.execute(query_inact, (value, )))
elif len(sys.argv) == 1:
    print('-' * 70)
    print('Active values:')
    print('-' * 70)
    output_with_0args(conn.execute('select * from dhcp where active = 1'))
    print('-' * 70)
    print('Inactive values:')
    print('-' * 70)
    output_with_0args(conn.execute('select * from dhcp where active = 0'))
else:
    print('Пожалуйста, введите два или ноль аргументов')


