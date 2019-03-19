#!/usr/bin/env python3.6

import re

def return_match(file,regex):
    '''
    Return list of match regex
    '''
    result = []
    with open(file,'r') as f:
        for line in f:
            match = re.search(regex,line)
            if match:
                result.append(match.group())
    return(result)

def parse_cfg(file):
    '''
    Return list of tuples with ip addr and mask of interfaces
    task_15_3
    '''
    result = []
    with open(file,'r') as f:
        for line in f:
            match = re.search('ip address (\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+)',line)
            if match:
                result.append((match.group(1),match.group(2)))
    return(result)

def parse_cfg_a(file):
    '''
    Return dict of tuples with ip addr and mask of interfaces
    interface is a key
    task_15_3a
    '''
    result = {}
    with open(file,'r') as f:
        for item in f.read().split('!'):
            match_int = re.search('interface \w+\d+(/\d+)?',item)
            if match_int:
                match_ip = re.search('ip address (\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+)',item)
                if match_ip:
                    result[match_int.group()] = (match_ip.group(1),match_ip.group(2))
    return(result)


def parse_cfg_b(file):
    '''
    Return dict of tuples with ip addr and mask of interfaces
    interface is a key
    task_15_3b
    '''
    result = {}
    with open(file,'r') as f:
        for item in f.read().split('!'):
            match_int = re.search('interface \w+\d+(/\d+)?',item)
            if match_int:
                match_ip = re.findall('ip address (\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+)',item)
                if match_ip:
                    result[match_int.group()] = match_ip
    return(result)

#returned = return_match('sh_ip_int_br.txt','([0-9]+\.)+[0-9]+')
returned = parse_cfg_b('config_r2.txt')
print(returned)
