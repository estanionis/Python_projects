#! /usr/bin/env python3
'''
Programa suskaiciuojanti paprastuosius skaicius
'''
SKAICIUS = input('Iveskite skaiciu = ')
DALMUO = 1
while DALMUO <= int(SKAICIUS):
    if SKAICIUS % DALMUO == 0:
        print(DALMUO)
    DALMUO = DALMUO + 1
input('Press enter to close program ')
