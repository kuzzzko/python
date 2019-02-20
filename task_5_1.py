#!/usr/bin/env python3
from sys import argv #task_5.1b

#ip_mask = argv[1] task_5.1b
ip_mask = input('Please enter IP address in format x.x.x.x/bitmask: ')

ip_list = ip_mask.split('/')[0].split('.')

bitmask = int(ip_mask.split('/')[1])
mask_bin_str = '1' * bitmask + '0' * (32 - bitmask)
mask_bin_list = [int(mask_bin_str[0:8],2),int(mask_bin_str[8:16],2),int(mask_bin_str[16:24],2),int(mask_bin_str[24:32],2)]

ip_bin_list = ['{0:08b}'.format(int(octet)) for octet in ip_mask.split('/')[0].split('.')]
ip_network_str = ''.join(ip_bin_list)[0:bitmask] + '0' * (32 - bitmask)
ip_network_list = [int(ip_network_str[0:8],2),int(ip_network_str[8:16],2),int(ip_network_str[16:24],2),int(ip_network_str[24:32],2)]


ip_template = '''
    IP address:
    {0:<8}  {1:<8}  {2:<8}  {3:<8}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''

mask_template = '''
    Mask:
    /{4:<}
    {0:<8}  {1:<8}  {2:<8}  {3:<8}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''

net_template = '''
    Network:
    {0:<8}  {1:<8}  {2:<8}  {3:<8}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''

print(ip_template.format(int(ip_list[0]),int(ip_list[1]),int(ip_list[2]),int(ip_list[3])))
print(mask_template.format(mask_bin_list[0],mask_bin_list[1],mask_bin_list[2],mask_bin_list[3],bitmask))
print(net_template.format(ip_network_list[0],ip_network_list[1],ip_network_list[2],ip_network_list[3]))