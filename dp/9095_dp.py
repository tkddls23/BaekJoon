# 9095 1,2,3 더하기
from sys import stdin 
from itertools import permutations

T = int(stdin.readline())
cases = []
test = [1,2,3]

def dp(case):
    if case <=3:
        d = [1,2,4]
        return d[case-1]
    elif case > 3:
        d = [1,2,4] + [0]*(case-3)
        for i in range(3,case):
            d[i] = d[i-3] + d[i-2] + d[i-1]
        return d[-1]

for i in range(T):
    cases.append(int(stdin.readline()))

for case in cases:
    print(dp(case))
