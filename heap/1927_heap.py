# 1927 최소 힙
import heapq
from sys import stdin 

n = int(stdin.readline())
q = []

for _ in range(n):
    x = int(stdin.readline())

    if x == 0:
        if len(q) != 0:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(n, x)
