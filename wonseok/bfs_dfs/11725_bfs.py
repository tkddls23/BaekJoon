# 11725 트리의 부모 찾기
from sys import stdin
from collections import deque

n = int(stdin.readline())

graph = [[i] for i in range(n+1)]
visit = [False] * (n + 1)
parent = [0] * (n + 1)
for i in range(n - 1):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(V):
    queue = deque([V])
    visit[V] = True
    while queue:
        V = queue.popleft()
        for i in graph[V]:
            if not visit[i]:
                parent[i] = V
                visit[i] = True
                queue.append(i)


bfs(1)

for i in range(2, n + 1):
    print(parent[i])

# 메모리 초과 남
# n = int(stdin.readline())
# 
# graph = [[0] * (n+1) for _ in range(n+1)]
# visit=[False]*(n+1)
# parent = [0]*(n+1)
# for i in range(n-1):
#     u, v = map(int, stdin.readline().split())
#     graph[u][v] = graph[v][u] = 1
# 
# def bfs(V):
#     queue =deque([V])
#     visit[V] = True
#     while queue:
#         V = queue.popleft()
#         for i in graph[V]:
#             if not visit[i]:
#                 parent[i] = V
#                 visit[i] = True
#                 queue.append(i)
# bfs(1)
# 
# for i in range(2,n+1):
#     print(parent[i])
