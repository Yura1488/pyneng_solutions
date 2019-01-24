#!/usr/bin/env python3
"""
Задание 7.3b
Сделать копию скрипта задания 7.3a

Дополнить скрипт:

Запросить у пользователя ввод номера VLAN.
Выводить информацию только по указанному VLAN.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
vlan = input('Введите VLAN ID: ')
with open('CAM_table.txt', 'r') as start:
    lists = [] 
    for line in start: 
        if line.count('.') == 2: 
            a = line.strip('\n').split() 
            a.pop(-2) 
            if a[0] == vlan:
                print(a[0] + '    ' + a[1] + '   ' + a[2])

"""
09:25 $ ./7.3b.py 
Введите VLAN ID: 100
100    01bb.c580.7000   Gi0/1
100    0a1b.1c80.7000   Gi0/4
09:26 $ ./7.3b.py 
Введите VLAN ID: 200
200    0a4b.c380.7000   Gi0/2
200    1a4b.c580.7000   Gi0/6
09:26 $ ./7.3b.py 
Введите VLAN ID: 300
300    a2ab.c5a0.7000   Gi0/3
300    0a1b.5c80.7000   Gi0/7
09:26 $ ./7.3b.py 
Введите VLAN ID: 400
"""