#dp[n][m] = dp[n-1][m] + dp[n][m-1]  

def solution(m, n, puddles):
    arr = [[0]*m for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    
    for p in puddles:
        arr[p[1]-1][p[0]-1] = 1
    
    #initialize
    dp[0][0] = 1    
    for i in range(n):
        if(arr[i][0]):
            break
        dp[i][0] = 1
        
    for i in range(m):
        if(arr[0][i]):
            break
        dp[0][i] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if(not arr[i][j]):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

              
    return dp[n-1][m-1] % 1000000007
    