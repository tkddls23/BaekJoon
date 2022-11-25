# 1260 DFS BFS
from sys import stdin
from collections import deque

N, M, V = map(int, stdin.readline().split())
# 행렬
matrix = [[0] * (N + 1) for _ in range(N + 1)]
# 탐색한 곳
visited = [0] * (N + 1)

for i in range(M):
    a, b = map(int, stdin.readline().split())
    # 중복 방지
    matrix[a][b] = matrix[b][a] = 1


def dfs(V):
    visited[V] = 1
    print(V, end=' ')

    for i in range(1, N + 1):
        if visited[i] == 0 and matrix[V][i] == 1:
            dfs(i)


def bfs(V):
    queue = deque()
    queue.append(V)
    visited[V] = 1

    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N + 1):
            if visited[i] == 0 and matrix[V][i] == 1:
                queue.append(i)
                visited[i] = 1


dfs(V)
visited = [0 for i in range(N + 1)]
print()
bfs(V)
