#!/bin/python

import sys


n = int(raw_input().strip())
squares = map(int, raw_input().strip().split(' '))
d,m = raw_input().strip().split(' ')
d,m = [int(d),int(m)]
# your code goes here

num_ways = 0
for i in range(len(squares)-m+1):
    if sum(squares[i:i+m]) == d:
        num_ways += 1
        

print num_ways
    