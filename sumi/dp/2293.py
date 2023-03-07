import sys

sys.stdin = open('index.txt')
input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

if __name__ == '__main__':
    # 사용한 동전의 구성이 같은데 순서만 다른것은 같은 경우
    # => 조합 문제

    n, k = map(int, input().split())
    coin = [int(input()) for i in range(n)]

    dp = [0 for i in range(k+1)]
    dp[0] = 1

    for c in coin:
        for t_k in range(c, k+1):
            if t_k - c >= 0:
                dp[t_k] += dp[t_k - c]

    print(dp[k])

