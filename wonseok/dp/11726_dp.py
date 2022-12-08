# 11726 2Xn 타일링
from sys import stdin 

n = int(stdin.readline())

test = [1,2]

def dp(case):
    if case <=4:
        d = [1,2,3,5]
        return d[case-1]
    elif case > 4:
        d = [1,2,3,5] + [0]*(case-4)
        for i in range(4,case):
            d[i] =  d[i-2] + d[i-1]
        return d[-1]


print(dp(n) % 10007)




