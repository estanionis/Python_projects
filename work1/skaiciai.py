#! /usr/bin/python3
'''
Programa suskaiciuojanti paprastuosius skaicius
'''
SKAICIUS = input('Iveskite skaiciu = ')
DALMUO = 1
while DALMUO <= int(SKAICIUS):
    if int(SKAICIUS) % int(DALMUO) == 0:
        print(DALMUO)
    DALMUO = DALMUO + 1