#!/usr/bin/env python3

def generate_access_config(access, psecurity=False):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех портов в режиме access
    с конфигурацией на основе шаблона
    '''
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
#Task_9_1
    access_cfg_list = []
    for intf, vlan in access.items():
      access_cfg_list.append('interface ' + intf)
      for command in access_template:
        if 'access vlan' in command:
          access_cfg_list.append(command + ' ' + str(vlan))
        else:
          access_cfg_list.append(command)
      if psecurity:
        for command in port_security:
          access_cfg_list.append(command)
    #print(access_cfg_list)
#Task_9_1b
    access_cfg_list = []
    access_cfg_dict = {}
    for intf, vlan in access.items():
      for command in access_template:
        if 'access vlan' in command:
          access_cfg_list.append(command + ' ' + str(vlan))
        else:
          access_cfg_list.append(command)
      if psecurity:
        for command in port_security:
          access_cfg_list.append(command)
      access_cfg_dict['interface ' + intf] = access_cfg_list
    #print(access_cfg_list)
    print(access_cfg_dict)


access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

generate_access_config(access_dict, psecurity=True)
