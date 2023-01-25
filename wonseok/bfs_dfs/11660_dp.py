# 11660 구간 합 구하기 5
from sys import stdin


def dp(x1, y1, x2, y2, prefixSum):
    return prefixSum[x2][y2] - prefixSum[x1 - 1][y2] - prefixSum[x2][y1 - 1] + prefixSum[x1 - 1][y1 - 1]


n, m = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
prefixSum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + matrix[i - 1][j - 1]

for i in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(dp(x1, y1, x2, y2, prefixSum))
