#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''программа рисует в консоли елочку'''
'''             *
               ***
              *****
             *******
            *********
           ***********
'''

#Пример - 1
for i in range(1, 20, 2):  #функция range() указывает начальное значение, конечное значение и шаг.
    print('{:^20}'.format('*' * i))  # Печатаем символ выравнивая его по центру



#Пример -2
SPACE = ' '
STRAR = '*'

rows = int(input('Укажите размер ёлочки: '))
spaces = rows-1
stars = 1

for i in range(rows):
    print(
        (SPACE*spaces) +
        (STRAR*stars) +
        (SPACE*spaces)
    )
    stars += 2
    spaces -= 1
