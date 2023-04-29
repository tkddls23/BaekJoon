from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

dx = [[-1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, 1]]
dy = [[0, 0, 1], [0, 0, -1], [-1, 0, 0], [1, 0, 0]]
visited = [[0]*m for _ in range(n)]

ans = 0
def dfs(y, x, cnt):
    global ans

    if x == m:
        y += 1
        x = 0
    
    if y == n:
        ans = max(ans, cnt)
        return

    for i in range(4):
        flag = True
        for j in range(3):
            ny = y + dy[i][j]
            nx = x + dx[i][j]

            if ny<0 or nx<0 or ny>=n or nx>=m:
                flag = False
                break
            
            if visited[ny][nx]:
                flag = False
                break
          
        if not flag:
            continue
        
        y1, y2 = y+dy[i][0], y+dy[i][2]
        x1, x2 = x+dx[i][0], x+dx[i][2]
        
        ncnt = cnt + (arr[y][x]*2 + arr[y1][x1] + arr[y2][x2])
        visited[y][x] = 1
        visited[y1][x1] = 1
        visited[y2][x2] = 1
        
        dfs(y, x+1, ncnt)

        visited[y][x] = 0
        visited[y1][x1] = 0
        visited[y2][x2] = 0

    dfs(y, x+1, cnt)
        
if n <= 1 or m <= 1:
    print(0)
else:
    dfs(0, 0, 0)
    print(ans)