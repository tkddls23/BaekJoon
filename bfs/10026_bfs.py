# 10026 적록색약
from collections import deque
n = int(input())
matrix = []
rg_matrix = []

for _ in range(n):
    tmp = list(input())
    tmp2 = tmp.copy()
    matrix.append(tmp)
    rg_matrix.append(tmp2)


for i in range(n):
    for j in range(n):
        if rg_matrix[i][j] == 'G':
            rg_matrix[i][j] = 'R'

rgb_cnt = 0
rg_cnt = 0

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rg_bfs(x, y):
    if rg_matrix[x][y] == 'R':
        color = 'R'
    else:
        color = 'B'

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 상하좌우로 탐색한다
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표가 matrix 범위 밖일때
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if rg_matrix[nx][ny] == color:
                rg_matrix[nx][ny] = 'x'
                queue.append([nx, ny])

def rgb_bfs(x, y):
    if matrix[x][y] == 'R':
        color = 'R'
    elif matrix[x][y] == 'G':
        color = 'G'
    else:
        color = 'B'

    queue = [[x, y]]
    while queue:
        x, y = queue.pop()

        for i in range(4):  # 상하좌우로 탐색한다
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표가 matrix 범위 밖일때
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if matrix[nx][ny] == color:
                matrix[nx][ny] = 'x'
                queue.append([nx, ny])

for x in range(n):
     for y in range(n):
         # 이미 지나간 곳 인지
        if matrix[x][y] != 'x':
            rgb_bfs(x, y)
            matrix[x][y] = 'x'
            rgb_cnt += 1

for x in range(n):
    for y in range(n):
        # 이미 지나간 곳 인지
        if rg_matrix[x][y] != 'x':
            rg_bfs(x, y)
            rg_matrix[x][y] = 'x'
            rg_cnt += 1

print(f'{rgb_cnt} {rg_cnt}')
