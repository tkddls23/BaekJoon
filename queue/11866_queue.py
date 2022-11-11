# 11866 요세푸스 문제 0
import sys

NK = list(map(int,sys.stdin.readline().split()))
N = NK[0]
K = NK[1]
arr = [i for i in range(1,N+1)]
result = []
tmp = 0

for i in range(N):
    tmp += K-1  
    if tmp >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        tmp = tmp%len(arr)
    result.append(str(arr.pop(tmp)))

print("<",", ".join(result)[:],">", sep='')