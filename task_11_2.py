#!/usr/bin/env python3.6

from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology

files = ['sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt','sh_cdp_n_sw1.txt']

dict_unique = {}
for namefile in files:
    with open(namefile,'r') as file:
        dict_part = parse_cdp_neighbors(file.read())
    for key_part,value_part in dict_part.items():
        if not any(key == value_part for key in dict_unique.keys()):
            dict_unique[key_part] = value_part

draw_topology(dict_unique)