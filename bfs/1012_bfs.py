# 1012 유기농 배추

from sys import stdin  

t = int(stdin.readline())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = [[x,y]]
    while queue:
        x,y = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny <0 or ny >= M:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append([nx,ny])

for i in range(t):
    M, N, K = map(int,input().split())
    matrix = [[0]*(M) for _ in range(N)]
    cnt = 0

    for j in range(K):
        a,b = map(int,input().split())
        matrix[b][a] = 1
    
    for x in range(N):
        for y in range(M):
            if matrix[x][y] == 1:
                bfs(x,y)
                matrix[x][y] = 0
                cnt += 1    
    print(cnt)