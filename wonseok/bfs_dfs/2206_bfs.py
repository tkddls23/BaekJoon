from sys import stdin
from collections import deque

n, m = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(n)]
result = [[[0] * 2 for _ in range(m)] for _ in range(n)]
result[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, flag = queue.popleft()

        if x == n - 1 and y == m - 1:
            return result[x][y][flag]

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a < 0 or a >= n or b < 0 or b >= m:
                continue
            if matrix[a][b] == 0 and result[a][b][flag] == 0:
                result[a][b][flag] = result[x][y][flag] + 1
                queue.append((a, b, flag))
            if matrix[a][b] == 1 and flag == 0:
                result[a][b][1] = result[x][y][0] + 1
                queue.append((a, b, 1))
    return -1


print(bfs())
