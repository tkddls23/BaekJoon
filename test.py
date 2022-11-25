from sys import stdin
from collections import deque

t = int(stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            my = y + dy[i]
            if (nx < 0 or nx >= n) or (my < 0 or my >= m):
                continue
            if matrix[nx][my] == 1:
                queue.append([nx, my])
                matrix[nx][my] = 0


for _ in range(t):
    m, n, k = map(int, stdin.readline().split())
    matrix = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, stdin.readline().split())
        matrix[b][a] = 1

    for x in range(n):
        for y in range(m):
            if matrix[x][y] == 1:
                bfs(x, y)
                matrix[x][y] = 0
                cnt += 1
    print(cnt)
