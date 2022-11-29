# 11727 2xn 타일링 2
from sys import stdin

n = int(stdin.readline())


def dp(case):
    if case <=4:
        d = [1,3,5,11]
        return d[case-1]
    elif case > 4:
        d = [1,3,5,11] + [0]*(case-4)
        for i in range(4,case):
            d[i] = d[i-2] * 2 + d[i-1]
        return d[-1]


print(dp(n) % 10007)