from sys import stdin
from collections import deque

n = int(stdin.readline())
matrix = [list(map(int, stdin.readline().strip())) for _ in range(n)]
visit = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    cnt = 0

    while queue:
        x,y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append([nx,ny])
    visit.append(cnt)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            matrix[i][j] = 0
            bfs(i,j)
visit.sort()
print(len(visit))
for k in visit:
    print(k)
