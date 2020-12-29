#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while(len(arr) > 0):
    mn = min(arr)
    print(len(arr))
    for _ in range(0,arr.count(mn)):
        arr.remove(mn)