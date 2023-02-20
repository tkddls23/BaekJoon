# # 2156 포도주 시식
from sys import stdin

n = int(stdin.readline())
glasses = [0] * 10000

for i in range(n):
    glasses[i] = int(stdin.readline())

dp = [0] * (n+1)
dp[0] = glasses[0]
dp[1] = glasses[0] + glasses[1]

for i in range(2, n):
    dp[i] = max(dp[i - 2] + glasses[i], dp[i - 1], dp[i - 3] + glasses[i - 1] + glasses[i])
print(dp[n - 1])



'''
# # 2156 포도주 시식
from sys import stdin

n = int(stdin.readline())
glasses = [int(input()) for i in range(n)]

    
dp = [0] * (n+1)
dp[0] = glasses[0]
dp[1] = glasses[0] + glasses[1]

for i in range(2, n):
    dp[i] = max(dp[i - 2] + glasses[i], dp[i - 1], dp[i - 3] + glasses[i - 1] + glasses[i])
print(dp[n - 1])
'''