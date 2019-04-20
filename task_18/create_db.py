#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import os
import sqlite3

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema2.sql'
db_exists = os.path.exists(db_filename)

if not db_exists:
    print('Creating schema...')
    conn = sqlite3.connect(db_filename)
    with open(schema_filename, 'r') as f:
        schema = f.read()
    conn.executescript(schema)
    print('Done')
    conn.close()
else:
    print('Database exists, assume dhcp table does, too.')
