# 11724 연결 요소의 개수

from sys import stdin 
from collections import deque

n, m = map(int, stdin.readline().split())

graph = [[0] * (n+1) for _ in range(n+1)]
vector = [0] * (n+1)
cnt =0

for i in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u][v] = graph[v][u] = 1

def bfs(V):
    queue =deque([V])
    vector[V] = 1
    while queue:
        V = queue.popleft()
        for i in range(1,n+1):
            if(vector[i] == 0 and graph[V][i] == 1):
                vector[i] = 1
                queue.append(i) 

for i in range(1,n+1):
    if vector[i] ==0:
        bfs(i)
        cnt += 1
print(cnt)