from sys import stdin

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]

dp = [0]*n
dp[0] = arr[0]

if n <= 2:
    print(sum(arr))
else:
    dp[1] = arr[0] + arr[1]

    for i in range(2, n):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
    
    print(dp[n-1])
