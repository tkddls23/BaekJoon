# 15657 n과 m(8)
from sys import stdin
from itertools import *

n, m = map(int, stdin.readline().split())
numbers = list(map(int, stdin.readline().split()))
numbers.sort()
result = []


def dfs(start):
    if len(result) == m:
        print(*result)
        return

    for i in range(start, n):
        result.append(numbers[i])
        dfs(i)
        result.pop()


dfs(0)
