#!/usr/bin/env python3

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

port_vlan_dict = dict(access='Enter vlan(s): ',trunk='Enter allowed VLANs: ')
port_type_dict = dict(access=access_template, trunk=trunk_template)

port_type = input('Enter interface mode (access/trunk): ')
interface = input('Enter interface type and number: ')
vlan = input(port_vlan_dict[port_type])

print('\n' + '-' * 30 + '\n')
print('interface '+ interface)
print('\n'.join(port_type_dict[port_type]).format(vlan))