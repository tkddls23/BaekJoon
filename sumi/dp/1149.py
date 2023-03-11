import sys

sys.stdin = open('index.txt')
input = sys.stdin.readline

def main(n,arr):
    dp = [[0 for _ in range(3)] for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][0] = min(dp[i-1][1] , dp[i-1][2]) + arr[i-1][0]
        dp[i][1] = min(dp[i-1][0] , dp[i-1][2]) + arr[i-1][1]
        dp[i][2] = min(dp[i-1][1] , dp[i-1][0]) + arr[i-1][2]

    return min(dp[n])

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        t = list(map(int, input().split()))
        arr.append(t)

    print(main(n,arr))
