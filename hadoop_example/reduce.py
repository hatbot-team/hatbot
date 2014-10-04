#!/bin/python3

import sys

prev = ''
cnt = 0
for x in sys.stdin.readlines():
    q, w = x.split('\t')[0], int(x.split('\t')[1])
    if (prev == q):
        cnt += 1
    else:
        if (cnt > 0):
            print(prev + '\t' + str(cnt))
        prev = q
        cnt = w
if (cnt > 0):
    print(prev + '\t' + str(cnt))
