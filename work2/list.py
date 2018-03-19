#! usr/bin/python3
"""
LIST
"""
LIST1 = [1, 2]
LIST2 = [2, 3]
LIST3 = [3, 4]
LIST4 = [4, 5]
print('List1 =', LIST1)
print('List2 =', LIST2)
print('List3 =', LIST3)
print('List4 =', LIST4)
LIST1.extend(LIST2)
print('List1.extend =', LIST1)
LIST2.append(LIST3)
print('List3.append =', LIST2)
LIST4.insert(1, 'inserted value')
print('List4.insert =', LIST4)
VAR = ['bar']
NEW_VAR = VAR
VAR.append('foo')
VAR[0] = 'baz'
print(NEW_VAR)
NEW_VAR1 = NEW_VAR.pop(0)
print('popped value is "{}"'.format(NEW_VAR1))
MULTI = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
for row in MULTI:
    print(row)
    for element in row:
        print('element: ', element)
