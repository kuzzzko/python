#!/usr/bin/env python3

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
MAC = 'AAAA:BBBB:CCCC'
IP = '192.168.3.1'
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
VLANS_uniqe = list(set(VLANS))
VLANS_uniqe.sort()

VLANS_list = list(set([int(vlan) for vlan in command1.split()[-1].split(',')]) & set([int(vlan) for vlan in command2.split()[-1].split(',')]))


ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route_list = ospf_route.split()

ospf_template = '''
    Protocol:           {:<}SPF
    Prefix:             {:<}
    AD/Metric:          {:<}
    Next-Hop:           {:<}
    Last Update:        {:<}
    Outbound Interface: {:<}
    '''

ip_template = '''
    IP address:
    {0:<8}  {1:<8}  {2:<8}  {3:<8}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''

ip_list = IP.split('.')

print(NAT.replace('Fast','Gigabit'))
print(MAC.replace(':','.'))
print(CONFIG.split()[-1].split(','))
print(VLANS_uniqe)
print(VLANS_list)
print(ospf_template.format(ospf_route_list[0],ospf_route_list[1],ospf_route_list[2].strip('[]'),ospf_route_list[4].rstrip(','),ospf_route_list[5].rstrip(','),ospf_route_list[6]))
print('{:b}{:b}{:b}'.format(int(MAC.split(':')[0],16),int(MAC.split(':')[1],16),int(MAC.split(':')[2],16)))
print(ip_template.format(int(ip_list[0]),int(ip_list[1]),int(ip_list[2]),int(ip_list[3])))