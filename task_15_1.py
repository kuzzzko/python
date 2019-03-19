#!/usr/bin/env python3.6

import re
from sys import argv

file, regex = argv[1:3]

with open(file,'r') as f:
    for line in f:
        match = re.search(regex,line)
        if match:
            print(line)

#task_15_1a - '0/[1,3]'
#task_15_1b - '0/[1,3]'
#task_15_1c - '/[1,3] '