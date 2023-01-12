# 11053 가장 긴 증가하는 부분 수열
from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
d = [0] * n


def dp():
    for i in range(n):
        for j in range(n):
            if a[i] > a[j]:
                d[i] = max(d[i], d[j])
        d[i] += 1
    return max(d)


print(dp())
