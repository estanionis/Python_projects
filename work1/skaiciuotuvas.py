#! /usr/bin/env python3
'''
Programa skaiciuojanti dvieju zenklu suma
'''
SKAICIUS = input('Iveskite pirma skaiciu ')
SKAICIUS1 = input('Iveskite antra skaiciu ')
ZENKLAS = input('Iveskite zenkla ')
if str(ZENKLAS) == '+':
    print('Suma lygi =', float(SKAICIUS) + float(SKAICIUS1))
elif str(ZENKLAS) == '-':
    print('Suma lygi =', float(SKAICIUS) - float(SKAICIUS1))
input('Press enter to close program ')
