#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sqlite3
import glob
import re
import yaml

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print(dhcp_snoop_files)

regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

dhcp_snooping_dict = {}

for file in dhcp_snoop_files:
    hostname = file[0:file.find('_')]
    dhcp_snooping_dict[hostname] = []
    with open(file) as data:
        for line in data:
            match = regex.search(line)
            if match:
                dhcp_snooping_dict[hostname].append(match.groups())

with open('switches.yml') as f:
    switches_dict = yaml.load(f)

print('Inserting DHCP Snooping data')
#print(dhcp_snooping_dict)
#print(switches_dict['switches'].keys())

conn = sqlite3.connect(db_filename)

for hostname,location in switches_dict['switches'].items():
    try:
        with conn:
            query = '''insert into switches (hostname, location)
                       values (?, ?)'''
            conn.execute(query, (hostname,location))
    except sqlite3.IntegrityError as e:
        print('Error occured: ', e)

for key,value_list in dhcp_snooping_dict.items():
    for row in value_list:
        try:
            with conn:
                query = '''insert into dhcp (mac, ip, vlan, interface, switch) 
                values (?, ?, ?, ?, '{}')'''.format(key)
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)

conn.close()