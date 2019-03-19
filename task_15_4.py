#!/usr/bin/env python3.6

import re

def parse_sh_ip_int_br(file):
    with open(file,'r') as f:
        result = re.findall('(?P<interface>\S+)\s+'
                            '(?P<address>[\d\.]+|unassigned)\s+\w+\s+\w+\s+'
                            '(?P<status>up|down|administratively down)\s+'
                            '(?P<protocol>up|down)',f.read())
    return(result)

if __name__ == "__main__":
    print(parse_sh_ip_int_br('sh_ip_int_br_2.txt'))