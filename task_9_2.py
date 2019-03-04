#!/usr/bin/env python3

def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    trunk_cfg_list = []
    trunk_cfg_dict = {}
    for intf, vlans in trunk.items():
        for command in trunk_template:
            if 'allowed vlan' in command:
                trunk_cfg_list.append(command + ' ' + ','.join(str(vlan) for vlan in vlans))
            else:
                trunk_cfg_list.append(command)
        trunk_cfg_dict[intf] = trunk_cfg_list
    return(trunk_cfg_dict)

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

trunk_cfg_list = generate_trunk_config(trunk_dict)
print(trunk_cfg_list)