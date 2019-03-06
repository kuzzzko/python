#!/usr/bin/env python3

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    return any(word in command for word in ignore)

def config_to_dict(file,*args):
    '''
    Func return dictionary where keys is a commands first level and values is a commands
    second level

    file - original configuration file
    *args - arguments for func ignore_command
    '''
    result = {}
    with open(file, 'r') as cfg:
        for line in cfg:
            if line.startswith('!') or ignore_command(line,*args) or not line.rstrip() or line.startswith(' !'):
                continue
            if not line.startswith(' '):
                cmd_first_lvl = line.rstrip()
                result[cmd_first_lvl] = []
            elif line.startswith(' ') and not line.startswith('  '):
                cmd_second_lvl = line.rstrip()
                result[cmd_first_lvl].append(cmd_second_lvl)
            elif line.startswith('  ') and type(result[cmd_first_lvl]) == list:
                result[cmd_first_lvl] = {key: [] for key in result[cmd_first_lvl]}
            if line.startswith('  ') and type(result[cmd_first_lvl]) == dict:
                result[cmd_first_lvl][cmd_second_lvl].append(line.rstrip())
    return(result)

ignore = ['duplex', 'alias', 'Current configuration']

config_dict = config_to_dict('config_r1.txt',ignore)

print(config_dict)