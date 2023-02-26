# 14502 바이러스
from sys import stdin
from collections import deque
import copy

n, m = map(int, input().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]

queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
answer = 0

# 백트래킹
def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                wall(cnt + 1)
                matrix[i][j] = 0


def bfs():
    global answer
    tmp_graph = copy.deepcopy(matrix)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                queue.append([i, j])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            if 0 <= ax < n and 0 <= ay < m and tmp_graph[ax][ay] == 0:
                tmp_graph[ax][ay] = 2
                queue.append([ax, ay])
    cnt = 0
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    answer = max(answer, cnt)


wall(0)
print(answer)
