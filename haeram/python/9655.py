from sys import stdin

n = int(stdin.readline())
dp = [0]*n

# 상근 = 1, 창영 = 2
dp[0] = 1
if n >= 2:
    dp[1] = 2
if n >= 3:
    dp[2] = 1

for i in range(3, n):
    if dp[i-1]==1 or dp[i-3]==1:
        dp[i] = 2
    else:
        dp[i] = 1

if dp[n-1] == 1:
    print('SK')
else:
    print('CY')