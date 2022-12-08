# 2775 부녀회장
import sys
T = int(sys.stdin.readline())
k = []
n = []
result = []
d = [[0 for col in range(15)] for row in range(15)]

def dp(k,n):
    if k == 0:
        return n
    if n == 1:
        return 1
    if d[k][n] != 0:
        return d[k][n]
    d[k][n] = dp(k,n-1) + dp(k-1,n)
    return d[k][n]

for i in range(0,T):
    k.append(int(sys.stdin.readline()))
    n.append(int(sys.stdin.readline()))
    result.append(dp(k[i],n[i]))


for i in range(T):
    print(result[i])