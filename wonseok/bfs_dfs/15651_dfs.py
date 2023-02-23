# 15651 n과 m (3)

from sys import stdin

n, m = map(int, stdin.readline().split())

s = []


def dfs(x):
    if len(s) == m:
        print(*s)
        return

    for i in range(x, n + 1):
        s.append(i)
        dfs(1)
        s.pop()


dfs(1)