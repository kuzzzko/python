#!/usr/bin/env python3

invlan = input('Please enter vlan: ')

#line_list = []
with open('CAM_table.txt','r') as src:
    #for line in src:
    #    if '.' in line:
            #task_7_3
            #print(line[0:26] + line[-6:-1])
    #        line_list.append(line)
    line_list = [line.split() for line in src if '.' in line]
    line_list.sort()
    for vlan, mac, _, intf in line_list:
        if invlan == vlan:
            print('{:6} {:} {:>8}'.format(vlan,mac,intf))
