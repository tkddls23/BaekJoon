from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
board = []

dz = [0, 0, 0, 0, 1, -1]
dy = [0, -1, 0, 1, 0, 0]
dx = [1, 0, -1, 0, 0, 0]

#set board
for _ in range(h):
    li = []
    for _ in range(n):
        li.append(list(map(int, stdin.readline().split())))

    board.append(li)

dq = deque()

#find rippen tomatos
for i in range(h):
    for j in range(n):
        for k in range(m):
            if(board[i][j][k] == 1):
                dq.append((i, j, k))


def bfs():
    while dq:
        z, y, x = dq.popleft()

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if(nz>=h or ny>=n or nx>=m or nz<0 or ny<0 or nx<0):
                continue
            if(board[nz][ny][nx] != 0):
                continue

            board[nz][ny][nx] = board[z][y][x]+1
            dq.append((nz, ny, nx))

bfs()

#check for 0 and get max in array
flag = True
arr_max = -1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if(board[i][j][k] == 0):
                flag = False

            arr_max = max(arr_max, board[i][j][k])

#print
if(not flag):
    print(-1)
elif(flag and arr_max == 1):
    print(0)
else:
    print(arr_max-1)




