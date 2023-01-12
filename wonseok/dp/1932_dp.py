# 1932 정수 삼각형
from sys import stdin

n = int(stdin.readline())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]
result[0][0] = matrix[0][0]

for i in range(n-1):
    for j in range(len(matrix[i])):
        result[i + 1][j] = max(result[i + 1][j], result[i][j] + matrix[i + 1][j])
        result[i + 1][j + 1] = result[i][j] + matrix[i + 1][j + 1]
print(max(result[-1]))