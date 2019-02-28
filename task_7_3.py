#!/usr/bin/env python3

vlan = input('Please enter vlan: ')

#line_list = []
with open('CAM_table.txt','r') as src:
    #for line in src:
    #    if '.' in line and vlan in line:
            #task_7_3
            #print(line[0:26] + line[-6:-1])
    #        line_list.append(line)
    line_list = [line.split() for line in src if '.' in line and vlan in line]
    line_list.sort()
    for vlan, mac, _, intf in line_list:
        print('{:6} {:} {:>8}'.format(vlan,mac,intf))
