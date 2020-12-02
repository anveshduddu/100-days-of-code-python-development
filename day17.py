import sys

count=0
n,k = map(int,input().strip().split(' '))
a = [int(a_temp) for a_temp in input().strip().split(' ')]
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        elif (i<j) and ((a[i]+a[j])%k==0):
            count+=1
print(count)