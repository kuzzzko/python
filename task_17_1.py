#!/usr/bin/env python3.6

import re
import csv
import glob

def parse_sh_version(output):
    '''
    func argument is output string command sh ver
    func return tuple of ios,image,uptime
    '''
    result = re.search('Cisco IOS.+Version (\S+),(.+\n)*'
                       'router uptime is (.+)\n(.+\n)*'
                       'System image file is "(\S+)"',output).group(1,5,3)
    return(result)

def write_to_csv(filename,data):
    with open(filename,'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)
headers = ['hostname', 'ios', 'image', 'uptime']
data = []
data.append(headers)
for file in sh_version_files:
    with open(file,'r') as f:
        f_str = f.read()
    hostname = re.search('n_(\S+)\.',file).group(1)
    sh_ver_list = list(parse_sh_version(f_str))
    sh_ver_list.insert(0,hostname)
    data.append(sh_ver_list)

write_to_csv('routers_inventory.csv',data)