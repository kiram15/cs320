#!/bin/python3

import sys
from collections import OrderedDict

string = OrderedDict()
val = input()

for i in sorted(val):
    if i in string:
        string[i] += 1
    else:
        string[i] = 1

for result in range(3):
    print(max(string, key=string.get), string.pop(max(string, key=string.get)))
