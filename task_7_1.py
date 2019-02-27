#!/usr/bin/env python3

ospf_template = '''
    Protocol:           {:<}SPF
    Prefix:             {:<}
    AD/Metric:          {:<}
    Next-Hop:           {:<}
    Last Update:        {:<}
    Outbound Interface: {:<}
    '''

with open('ospf.txt','r') as file:
    for line in file:
        l = line.split()
        print(ospf_template.format(l[0],l[1],l[2].strip('[]'),l[4].rstrip(','),l[5].rstrip(','),l[6]))