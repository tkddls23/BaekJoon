# 1697 숨바꼭질
from sys import stdin 
from collections import deque

max = 10**5
d = [0] * (max+1)
n, k = map(int,stdin.readline().split())

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(d[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<= nx <= max and d[nx] == 0:
                d[nx] = d[x] + 1
                queue.append(nx)

bfs()
