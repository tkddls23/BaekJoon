# 11050 이항 계수1
NK = list(map(int,input().split()))
N = NK[0]
K = NK[1]
result = 1
for i in range(N,N-K,-1):
    result *= i

for i in range(K,0,-1):
    result /= i

print(int(result))