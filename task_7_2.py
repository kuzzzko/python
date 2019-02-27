#!/usr/bin/env python3

from sys import argv

src_name, dst_name = argv[1::]
ignore = ['duplex', 'alias', 'Current configuration']

with open(src_name,'r') as src, open(dst_name,'w') as dst:
    src_list = src.readlines()
    for line in src_list:
        for command in ignore:
            if command in line:
               src_list[src_list.index(line)] = ''
    #7.2a
    #for out in src_list:
    #    if not out.startswith('!'):
    #        print(out.rstrip())
    dst.writelines(src_list)