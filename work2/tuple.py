#! usr/bin/env python3
"""
Programa perrasanti nauja tuple
"""
TUPLE1 = (1, 10, 'door', 'warm', True, False, None)
NEW_TUPLE = TUPLE2 = ()
for ITEM in TUPLE1:
    if not isinstance(ITEM, int):
        NEW_TUPLE += (ITEM, )
print(TUPLE1, '\n', NEW_TUPLE)

