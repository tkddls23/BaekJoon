# 9461 파도반 수열
from sys import stdin 

t = int(stdin.readline())


def dp(d,n):
    if n == 1:
        d[1] = 1
        return d[n]
    if n == 2:
        d[2] = 1
        return d[n]
    if n == 3:
        d[3]= 1
        return d[n]
    elif d[n] != 0:
        return d[n]
    else:
        d[n] = dp(d,n-3) + dp(d,n-2)
        return d[n]

for _ in range(t):
    n = int(stdin.readline())
    d = [0]* (n+1)
    print(dp(d,n))