# 7569 토마토 2
from collections import deque


m,n,h = map(int,input().split())
matrix = []
queue = deque([])

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(queue):
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            ax = x + dx[i]
            ay = y + dy[i]
            az = z + dz[i]
            if 0<=ax<h and 0<=ay<n and 0<=az<m and matrix[ax][ay][az]==0:
                    queue.append([ax,ay,az])
                    matrix[ax][ay][az] = matrix[x][y][z] + 1

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i,j,k])
    matrix.append(tmp)

bfs(queue)
result = 0
for i in matrix:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        result = max(result,max(j))

print(result -1)