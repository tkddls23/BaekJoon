# 15663 n과m(9)
from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())

arr = sorted(list(map(int, input().split())))
result = []
visit = [False] * n


def dfs():
    if len(result) == m:
        print(*result)
        return
    tmp = 0
    for i in range(n):
        if visit[i] or tmp == arr[i]:
            continue
        result.append(arr[i])
        visit[i] = True
        tmp = arr[i] # ex) 7 9 한 다음 또 7 9 나오는 경우 제외
        dfs()
        visit[i] = False
        result.pop()


dfs()
