from sys import stdin

n, k = map(int, stdin.readline().split()) # max time, subjects
weight = []
time = []

for i in range(k):
    w, t = map(int, stdin.readline().split())
    weight.append(w)
    time.append(t)

dp = [[0]*(n+1) for _ in range(k+1)]

for i in range(1, k+1):
    for j in range(1, n+1):
        if time[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i-1]] + weight[i-1])

print(dp[k][n])