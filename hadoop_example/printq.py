#!/bin/python3

fin = open('./output/part-00000')
a = []
for x in fin.readlines():
    a.append((int(x.split('\t')[1]), x.split('\t')[0]))

a.sort(reverse = True)
for i in range(100):
    print(a[i])
