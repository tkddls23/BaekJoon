# 14500 테트로미노
from sys import stdin
from collections import deque

# 상하좌우 탐색
def dfs(row, column, idx, total):
    global result
    # 최대값 가지치기
    if result >= total + maxValue * (3 - idx):
        return
    if idx == 3:
        result = max(result, total)
        return
    else:
        for i in range(4):
            nr = row + dx[i]
            nc = column + dy[i]
            if 0 <= nr < n and 0 <= nc < m and visit[nr][nc] == 0:
                # ㅗ 모양 만들기
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(row, column, idx + 1, total + matrix[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + matrix[nr][nc])
                visit[nr][nc] = 0


n, m = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
visit = [([0] * m) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
# 배열의 최대값 추출하기
maxValue = max(map(max, matrix))

for row in range(n):
    for column in range(m):
        visit[row][column] = 1
        dfs(row, column, 0, matrix[row][column])
        visit[row][column] = 0

print(result)
