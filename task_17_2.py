#!/usr/bin/env python3.6

import re
import glob
import yaml

def parse_sh_cdp_neighbors(sh_cdp_nei_str):
    result = {}
    hostname = re.search('(\S+)(>|#)',sh_cdp_nei_str).group(1)
    neighbors = re.findall('\n(?P<nei>\S+) +'
                           '(?P<loc_int>\w+ \S+) +.+'
                           '(?P<nei_int> \w+ \S+)\n',sh_cdp_nei_str)
    result[hostname] = {item[1]:{item[0]:item[2]} for item in neighbors}
    return(result)

sh_cdp_nei_files = glob.glob('sh_cdp*')
nei_dict = {}
for file in sh_cdp_nei_files:
    with open(file,'r') as f:
        nei_dict.update(parse_sh_cdp_neighbors(f.read()))
print(nei_dict)

with open('topology.yaml', 'w') as f:
    yaml.dump(nei_dict, f)

with open('topology.yaml') as f:
    print(f.read())