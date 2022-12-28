# 1149 RGB 거리
from sys import stdin

# 집의 수
n = int(stdin.readline())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    matrix[i][0] += min(matrix[i-1][1], matrix[i-1][2])
    matrix[i][1] += min(matrix[i-1][0], matrix[i-1][2])
    matrix[i][2] += min(matrix[i-1][0], matrix[i-1][1])
print(min(matrix[-1]))