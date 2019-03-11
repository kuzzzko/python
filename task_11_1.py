#!/usr/bin/env python3

def parse_cdp_neighbors(file_str):
    '''
    func return dict of tuples cisco cdp_neighbors
    argument is a line string file.
    '''
    localhost = file_str[:file_str.find('>')].strip()
    neighbors_list = file_str[file_str.find('Port ID\n') + 8:].strip().split('\n')
    result = {}
    for line in neighbors_list:
        #llist = [item.strip() for item in line.split('  ') if item]
        neighbor,local_int_type,local_int,*other,neighbor_int_type,neighbor_int = line.split()
        result[(localhost,local_int_type + local_int)] = (neighbor,neighbor_int_type + neighbor_int)
    return(result)

if __name__ == "__main__":
    with open('sh_cdp_n_r2.txt','r') as file:
        dict_neighbors = parse_cdp_neighbors(file.read())
        print(dict_neighbors)