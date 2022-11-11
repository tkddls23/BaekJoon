# 2667 단지번호붙이기
from sys import stdin 
from collections import deque


n = int(stdin.readline())
matrix = [list(map(int, input())) for _ in range(n)]
result = []


def bfs(x,y,mul):

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y))
    sum = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = mul
    for j in range(n):
        sum += matrix[j].count(mul)
    if matrix[x][y] == 1:
        sum = 1
    return sum


cnt = 2
for j in range(n):
    for k in range(n):
        if matrix[j][k] == 1:
            result.append(bfs(j,k,cnt))
            cnt +=1

result.sort()

print(len(result))
for i in result:
    print(i)