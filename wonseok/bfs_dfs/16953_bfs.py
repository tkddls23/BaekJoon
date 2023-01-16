# 16953 a -> b
from sys import stdin
from collections import deque

max = 10 ** 9
n, k = map(int, stdin.readline().split())

def bfs():
    queue = deque()
    queue.append((n,1))
    while queue:
        x,cnt = queue.popleft()
        if x == k:
            return cnt
        for nx in (x*2, int(str(x)+'1')):
            if 0 <= nx <= k:
                queue.append((nx,(cnt+1)))

result = bfs()

if result:
    print(result)
else:
    print(-1)
