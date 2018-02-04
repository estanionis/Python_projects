#! usr/bin/env python3
"""
LIST
"""
NOT_A_LIST = (1, 2)
LIST1 = [1, 2]
LIST2 = list(NOT_A_LIST)
print(LIST1 == LIST2, NOT_A_LIST == LIST1)
LIST1.append(3)
print('append() returns None: ', LIST1.append(4))
print(LIST1)
LIST1.append(LIST2)
