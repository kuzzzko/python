#!/usr/bin/env python3.6

import subprocess
from tabulate import tabulate

def ping_ip(ip_addr_list):
    '''
    Ping IP address and return two lists:
    available and unavailable addresses
    '''
    reach, unreach = [],[]
    for ip_addr in ip_addr_list:
        reply = subprocess.run(['ping','-c','3','-n','-W','1',ip_addr], stdout=subprocess.DEVNULL)
        if reply.returncode == 0:
            reach.append(ip_addr)
        else:
            unreach.append(ip_addr)
    return reach, unreach

def check_ip_range(ip_addr_list):
    '''
    Return list IP addr without range
    '''
    result = []
    for ip_addr in ip_addr_list:
        if '-' in ip_addr:
            ip_rng = '.'.join(ip_addr.split('-')[0].split('.')[:-1])
            frst_rng = int(ip_addr.split('-')[0].split('.')[-1])
            last_rng = int(ip_addr.split('-')[-1].split('.')[-1])
            for i in range(frst_rng,last_rng + 1):
                result.append(ip_rng + '.' + str(i))
        else:
            result.append(ip_addr)
    return(result)

def ip_table(available,unavailable):
    '''
    Print IP table reach and unreach
    input:
    2 list of ip addresses
    '''
    header = ['Reachable','Unreachable']
    result = []
    if len(available) > len(unavailable):
        temp_list = unavailable.copy()
        for item in range(0,len(available) - len(unavailable)):
            temp_list.append(' ')
        for item in range(0,len(available)):
            result.append([available[item],temp_list[item]])
    elif len(available) < len(unavailable):
        temp_list = available.copy()
        for item in range(0,len(unavailable) - len(available)):
            temp_list.append(' ')
        for item in range(0,len(unavailable)):
            result.append([temp_list[item],unavailable[item]])
    else:
        for item in range(0,len(available)):
            result.append([available[item],unavailable[item]])
    print(tabulate(result,headers=header))


ip_list = ['8.8.8.8','8.9.8.9','10.0.0.1','192.168.1.1','192.168.0.1','8.8.8.1-10']
ip_list_2 = ['8.9.8.1-10','8.8.8.8','192.168.1.1-192.168.1.10']

reach, unreach = ping_ip(check_ip_range(ip_list))
ip_table(reach,unreach)
