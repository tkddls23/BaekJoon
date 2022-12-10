# 11286 절댓값 힙
import heapq
from sys import stdin
n = int(stdin.readline())
q = []

for i in range(n):
    x = int(stdin.readline())
    if x == 0:
        if len(q) != 0:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(x),x))
