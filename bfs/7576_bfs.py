# 7576 토마토 1
from collections import deque


m,n = map(int,input().split())
matrix = []
queue = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(queue):
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            if 0 <= ax < n and 0 <= ay < m and matrix[ax][ay] == 0:
                queue.append([ax,ay])
                matrix[ax][ay] = matrix[x][y] + 1

for _ in range(n):
    matrix.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i,j])

bfs(queue)
result = 0
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result,max(i))

print(result -1)