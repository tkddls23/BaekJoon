from sys import stdin

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i >= n-1 and j >= n-1:
            print(dp[i][j])
            break
        
        # y 방향으로 이동
        if arr[i][j] + i < n:
            dp[i+arr[i][j]][j] += dp[i][j]

        if arr[i][j] + j < n:
            dp[i][j+arr[i][j]] += dp[i][j]