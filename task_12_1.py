#!/usr/bin/env python3.6

import subprocess

def ping_ip(ip_addr_list):
    '''
    Ping IP address and return two lists:
    available and unavailable addresses
    '''
    available = []
    unavailable = []
    for ip_addr in ip_addr_list:
        reply = subprocess.run(['ping','-c','3','-n','-W','1',ip_addr], stdout=subprocess.DEVNULL)
        if reply.returncode == 0:
            available.append(ip_addr)
        else:
            unavailable.append(ip_addr)
    return available, unavailable

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
    print(result)
    return(result)


ip_list = ['8.8.8.8','8.9.8.9','10.0.0.1','192.168.1.1','192.168.0.1','8.8.8.1-10']
ip_list_2 = ['8.9.8.1-10','8.8.8.8','192.168.1.1-192.168.1.10']

ok, not_ok = ping_ip(check_ip_range(ip_list_2))

print(ok)
print(not_ok)