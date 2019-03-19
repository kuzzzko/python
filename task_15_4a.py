#!/usr/bin/env python3.6

import re
from task_15_4 import parse_sh_ip_int_br

def convert_to_dict(headers,parse_show):
    result =[]
    for item in parse_show:
        result.append(dict(zip(headers,item)))
    return(result)

headers = ['interface', 'address', 'status', 'protocol']
print(convert_to_dict(headers,parse_sh_ip_int_br('sh_ip_int_br_2.txt')))