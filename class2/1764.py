# 1764 듣보잡
from sys import stdin 

N, M = map(int,stdin.readline().split())

listen = []
see = []

for i in range(N):
    listen.append(input())

for i in range(M):
    see.append(input())

setA = set(listen)
setB = set(see)

result = setA.intersection(setB)

print(len(result))
for i in sorted(result):
    print(i)