# 1389 케빈 베이컨의 6단계 법칙
from sys import stdin
from collections import deque

# 유저의 수, 친구 관계의 수
n, m = map(int, stdin.readline().split())

# 친구 관계 matrix
matrix = [[0] * (n + 1) for _ in range(n + 1)]

# 탐색한 곳
countList = [0] * (n + 1)

for i in range(m):
    a, b = map(int, stdin.readline().split())
    # 중복 방지
    matrix[a][b] = matrix[b][a] = 1


def bfs(v):
    cnt = 0
    queue = deque([[v, cnt]])

    while queue:
        v, cnt = queue.popleft()
        if not visited[v]:
            visited[v] = True
            countList[v] += cnt
            cnt += 1
            for i in range(1, n + 1):
                if matrix[v][i] == 1:
                    queue.append([i, cnt])


for i in range(1, n + 1):
    visited = [False] * (n + 1)
    bfs(i)
print(countList.index(min(countList[1:])))
