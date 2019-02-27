#!/usr/bin/env python3

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = [mac_addr.replace(':','.') for mac_addr in mac]
print(mac_cisco)