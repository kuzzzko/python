#!/usr/bin/env python3

def get_int_vlan_map(filename):
    '''
    filename - config file
    func return 2 dictionary where interface name is a key
    '''
    acc_vlan_map_dict = {}
    trun_vlan_map_dict = {}
    with open(filename, 'r') as cfg:
        for line in cfg:
            if 'interface ' in line:
                interface = line.rstrip()
                acc = False
            if 'switchport mode access' in line:
                acc = True
                acc_vlan_map_dict[interface] = 1
            if 'access vlan' in line and acc:
                acc_vlan_map_dict[interface] = int(line.split()[-1])
            if 'allowed vlan' in line and not acc:
                trun_vlan_map_dict[interface] = [int(vlan) for vlan in line.split()[-1].split(',')]
    return(acc_vlan_map_dict, trun_vlan_map_dict)


acc_vlan_map_dict,trun_vlan_map_dict = get_int_vlan_map('config_sw2.txt')

print(acc_vlan_map_dict)
print(trun_vlan_map_dict)