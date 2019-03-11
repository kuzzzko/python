#!/usr/bin/env python3.6

from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology

files = ['sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt','sh_cdp_n_sw1.txt']

dict_all = {}

for namefile in files:
    with open(namefile,'r') as file:
        dict_all.update(parse_cdp_neighbors(file.read()))

for item in dict_all.values():
    if item in dict_all.keys():
        dict_all[item] = None

dict_unique = {key : item for key,item in dict_all.items() if item != None}
draw_topology(dict_unique)