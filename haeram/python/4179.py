from sys import stdin
from collections import deque

r, c = map(int, stdin.readline().split())
arr = [list(stdin.readline().rstrip()) for _ in range(r)]

# get player and fire point
sy, sx = 0, 0
fy, fx = [], []
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'J':
            sy, sx = i, j

        if arr[i][j] == 'F':
            fy.append(i)
            fx.append(j)


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 먼저 불이 가는 경우의 수 업데이트
visited = [[0]*c for _ in range(r)]

dq = deque()
for i in range(len(fy)):
    dq.append((fy[i], fx[i]))
    visited[fy[i]][fx[i]] = 1

while dq:
    y, x = dq.popleft()

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]

        if ny < 0 or nx < 0 or ny >= r or nx >= c:
            continue

        if visited[ny][nx] or arr[ny][nx] == '#':
            continue

        dq.append((ny, nx))
        visited[ny][nx] = visited[y][x] + 1


# 사람이 갈 수 있는 길들
visited_h = [[0]*c for _ in range(r)]

dq = deque()
dq.append((sy, sx))
visited_h[sy][sx] = 1

ans = 0
while dq:
    if ans:
        break

    y, x = dq.popleft()

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]

        if ny < 0 or nx < 0 or ny >= r or nx >= c:
            ans = visited_h[y][x]
            break

        if arr[ny][nx] == '#' or visited_h[ny][nx]:
            continue

        if visited[ny][nx] != 0 and visited_h[y][x]+1 >= visited[ny][nx]:
            continue

        dq.append((ny, nx))
        visited_h[ny][nx] = visited_h[y][x] + 1


if ans:
    print(ans)
else:
    print('IMPOSSIBLE')
