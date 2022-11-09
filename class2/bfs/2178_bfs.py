# 2178 미로 탐색
from sys import stdin 
from collections import deque
n,m = map(int,stdin.readline().split())

road = []
for _ in range(n):
    road.append(list(map(int,input().rstrip())))

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and road[nx][ny] == 1:
                queue.append((nx, ny))
                road[nx][ny] = road[x][y] + 1 
    
    return road[n-1][m-1]


print(bfs(0,0))