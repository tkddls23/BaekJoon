# climbing stairs
from collections import deque

n = 6

test = [1,2]

def dp(case):
    if case <=3:
        d = [1,2,3]
        return d[case-1]
    if case > 3:
        d = [1,2,3] + [0]*(case-3)
        for i in range(3,case):
            d[i] = d[i-2] + d[i-1]
        return d[-1]


print()




s = Solution()
s.climbStairs(1)