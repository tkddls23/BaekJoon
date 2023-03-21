import sys
from collections import deque

sys.stdin = open('index.txt')
input = sys.stdin.readline


def rain_after(arr, rain_mount):
    n = len(arr)
    safe = [[True for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] <= rain_mount:
                safe[i][j] = False

    d = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = set()

    # for x in safe:
    #     print(x)
    def bfs(i,j):
        que = deque()
        que.append((i, j))

        while que:
            x,y = que.pop()
            visited.add((x,y))
            for dx, dy in d:
                nx, ny =x+dx, y + dy
                if 0<= nx < n and 0<=ny<n and safe[nx][ny] and (nx,ny) not in visited:
                    que.append((nx, ny))

    cnt =0
    for i in range(n):
        for j in range(n):
            if safe[i][j] == True and (i,j) not in visited:
                bfs(i,j)
                cnt +=1
    return cnt

if __name__ == '__main__':

    n = int(input())

    arr = []
    max_rain = 0
    for _ in range(n):
        t = list(map(int, input().split()))
        arr.append(t)
        max_rain = max(max_rain, max(t))

    res = 1
    for rain in range(1, max_rain+1):
        after = rain_after(arr, rain)
        res = max(res, after)
    print(res)