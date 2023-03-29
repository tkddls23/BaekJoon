import sys
from collections import deque

sys.stdin = open('index.txt')
input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())

    dp = [0] * (n + 1)
    arr = []
    k = 0

    for i in range(n):
        ti, pi = map(int, input().split())
        k = max(k, dp[i])
        if i + ti > n:
            continue
        dp[i + ti] = max(k + pi, dp[i + ti])


    print(max(dp))
