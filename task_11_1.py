#!/usr/bin/env python3

def parse_cdp_neighbors(file_str):
    '''
    func return dict of tuples cisco cdp_neighbors
    argument is a line string file.
    '''
    localhost = file_str[:file_str.find('>')]
    neighbors_list = file_str.rstrip().split('\n')[6::]
    result = {}
    for line in neighbors_list:
        llist = [item.strip() for item in line.split('  ') if item]
        neighbor,local_int,*other,neighbor_int = llist
        result[(localhost,local_int)] = (neighbor,neighbor_int)
    return(result)


with open('sw1_sh_cdp_neighbors.txt','r') as file:
    dict_neighbors = parse_cdp_neighbors(file.read())
    print(dict_neighbors)