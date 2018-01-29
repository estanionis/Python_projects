#! /usr/bin/env python3
"""
10 klausimu testas
"""
i = 0
KLAUSIMAS1 = input('Klausimas Nr.1 \nKiek bus 5 * 5 = ')
if float(KLAUSIMAS1) == 25:
    print('Atsakete teisingai')
    i = i + 1
else:
    print('Atsakete neteisingai')
KLAUSIMAS2 = input('Klausimas Nr.2 \nKiek bus 20 + 20 = ')
if float(KLAUSIMAS2) == 40:
    print('Atsakete teisingai')
    i = i + 1
else:
    print('Atsakete neteisingai')
KLAUSIMAS3 = input('Klausimas Nr.3 \nKokia programavimo kalba mokotes = ')
if len(KLAUSIMAS3) == 6:
    print('Atsakete teisingai')
    i = i + 1
else:
    print('Atsakete neteisingai')
print('Is viso teisingai atsakete', i)
input('Press enter to close program')
