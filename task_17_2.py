#!/usr/bin/env python3.6

import re
import glob
import yaml
from pprint import pprint
from draw_network_graph import draw_topology

def parse_sh_cdp_neighbors(sh_cdp_nei_str):
    result = {}
    hostname = re.search('(\S+)(>|#)',sh_cdp_nei_str).group(1)
    neighbors = re.findall('\n(?P<nei>\S+) +'
                           '(?P<loc_int>\w+ \S+) +.+ '
                           '(?P<nei_int>\w+ \S+)',sh_cdp_nei_str)
    result[hostname] = {item[1]:{item[0]:item[2]} for item in neighbors}
    return(result)

def generate_topology_from_cdp(list_of_files,save_to_file=True,topology_filename='topology.yaml'):
    nei_dict = {}
    for file in list_of_files:
        with open(file,'r') as f:
            nei_dict.update(parse_sh_cdp_neighbors(f.read()))
    if save_to_file:
        with open(topology_filename, 'w') as f:
            yaml.dump(nei_dict, f)
    pprint(nei_dict)

sh_cdp_nei_files = glob.glob('sh_cdp*')
generate_topology_from_cdp(sh_cdp_nei_files)

with open('topology.yaml') as f:
    nei_dict = yaml.load(f)
for_draw = {}
for host,int_dict in nei_dict.items():
    for intf,remote_dict in int_dict.items():
        for rem_host,rem_int in remote_dict.items():
            if not any(key==(rem_host,rem_int) for key in result.keys()):
                for_draw[(host,intf)] = (rem_host,rem_int)
draw_topology(for_draw,'task_17_2c_topology')