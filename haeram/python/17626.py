from sys import stdin
import math

n = int(stdin.readline())
dp = [0]*(n+1)

dp[1] = 1

for i in range(2, n+1):
    cand = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        cand = min(cand, dp[i - j**2])

    dp[i] = cand + 1

print(dp[n])