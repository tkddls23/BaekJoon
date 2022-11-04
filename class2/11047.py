# 11047 동전 0
from sys import stdin 

N,K = map(int, stdin.readline().split())

money = [int(stdin.readline()) for _ in range(N)]
cnt = 0

while K:
    tmp = [i for i in money if i<=K]

    if max:
        cnt += K // max(tmp)
        K %= max(tmp)

print(cnt)
    
