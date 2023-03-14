import sys

sys.stdin = open('index.txt')
input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

MAX = 1000000
if __name__ == '__main__':
    n, k = map(int, input().split())
    coin = [int(input()) for i in range(n)]
    coin.sort()
    dp = [MAX for i in range(k+1)]
    dp[0] = 1

    for c in coin:
        if c <= k:
            dp[c] = 1

    for c in coin:
        for t_k in range(c, k+1):
            if t_k - c >= 0:
                dp[t_k] = min(dp[t_k], dp[t_k - c] + 1)

    print(dp[k] if dp[k] != MAX else -1)