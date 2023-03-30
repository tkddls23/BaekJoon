def largestRectangle(n, a, b):
    dp = [[0] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i, n):
            min_height = min(b[i:j+1])
            width = sum(a[i:j+1])
            dp[i][j] = max(dp[i-1][j], min_height * width)
            min_height = min(a[i:j+1])
            width = sum(b[i:j+1])
            dp[i][j] = max(dp[i][j], min_height * width)
            ans = max(ans, dp[i][j])
    return ans




print(largestRectangle(1, [3], [14]))  # Expected output: 42 your code return 42 correct
print(largestRectangle(2, [3, 4], [4, 5]))  # Expected output: 32 but your code return 32 correct
print(largestRectangle(4, [3, 2, 4, 2], [3, 1, 7, 5]))  # Expected output: 36 but your code return 49 wrong
