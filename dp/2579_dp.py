# 2579 계단 오르기
from sys import stdin

n = int(stdin.readline())
point = [0] * (n+1)
d = [0] * (n+1)

for i in range(1,n+1):
    point[i] = int(stdin.readline())

def dp(n):
    if n == 0:
        return 0
    if n == 1:
        d[1] = point[1]
        return d[1]
    elif n == 2:
        d[2] = point[1]+point[2]
        return d[2]
    elif d[n] != 0:
        return d[n]
    else:
        d[n] = max(dp(n-2) + point[n], dp(n-3)+point[n-1]+point[n])
        return d[n]



print(dp(n))