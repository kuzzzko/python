#!/usr/bin/env python3

ip_addr = input('Please input IP address: ')
ip_correct = False

while not ip_correct:
    if len(ip_addr.split('.')) == 4:
        for octet in ip_addr.split('.'):
            if octet.isdigit():
                if int(octet) >= 0 and int(octet) <= 255:
                    ip_correct = True
                else:
                    ip_correct = False
                    print('Incorrect IPv4 address\n')
                    ip_addr = input('Please input IP address: ')
                    break
            else:
                 ip_correct = False
                 print('Incorrect IPv4 address\n')
                 ip_addr = input('Please input IP address: ')
                 break
    else:
        print('Incorrect IPv4 address\n')
        ip_addr = input('Please input IP address: ')

octet = int(ip_addr.split('.')[0])

if octet >= 1 and octet <= 223:
    print('unicast')
elif octet >= 224 and octet <= 239:
    print('multicast')
elif ip_addr == '255.255.255.255':
    print('local broadcast')
elif ip_addr == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
