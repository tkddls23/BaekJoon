# 2606 바이러스

from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())

computer = [[0] * (n+1) for i in range(n+1)]
virus = [0] * (n+1)

for i in range(m):
    a, b = map(int,stdin.readline().split())
    computer[a][b] = computer[b][a] = 1

def bfs(V):
    queue = deque()
    queue.append(V)
    virus[V] = 1
    cnt = 0

    while queue:
        V = queue.popleft()
        cnt +=1
        for i in range(1,n+1):
            if(virus[i] == 0 and computer[V][i] == 1):
                queue.append(i)
                virus[i] = 1
    return cnt 

print(bfs(1)-1)

