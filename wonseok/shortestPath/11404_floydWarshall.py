# 11404 플로이드
from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
matrix = [[100000000] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, stdin.readline().split())
    matrix[start][end] = min(cost, matrix[start][end])

for k in range(1, n + 1):  # 경로가 젤 위에 있어야 댐
    matrix[k][k] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for row in matrix[1:]:
    for i in range(1,n+1):
        if row[i] == 100000000:
            row[i] = 0
        print(row[i], end=" ")
    print()
