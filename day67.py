#!/bin/python3

import sys

def surfaceArea(A):
    H, W = len(A), len(A[0])
    area = 2*H*W

    
    for ind in range(H):
        for jnd in range(W):
            if ind-1 >= 0:
            
                area += max(0, A[ind][jnd] - A[ind-1][jnd])
            else:
            
                area += A[ind][jnd]
            
            if jnd-1 >= 0:
            
                area += max(0, A[ind][jnd] - A[ind][jnd-1])
            else:
            
                area += A[ind][jnd]
            
            if ind+1 < H:
            
                area += max(0, A[ind][jnd] - A[ind+1][jnd])
            else:
            
                area += A[ind][jnd]
            
            if jnd+1 < W:
                
                area += max(0, A[ind][jnd] - A[ind][jnd+1])
            else:
                
                area += A[ind][jnd]
    return area

if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
        A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
        A.append(A_t)
    result = surfaceArea(A)
    print(result)