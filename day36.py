#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
cur = 0
e = 100
while True:
    if c[cur]==1:
        e-=2
    e-=1
    cur = (cur+k)%n
    if cur==0:
        break
print e
    