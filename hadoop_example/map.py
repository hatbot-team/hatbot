#!/bin/python3

import sys
for x in sys.stdin.readlines():
    for i in x.split():
        q = ''
        for c in i:
            if str.isalpha(c):
                q = q + c
        if q != '':
            print(str.lower(q) + '\t' + str(1))
