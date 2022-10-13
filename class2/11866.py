# 11866 요세푸스 문제 0

NK = list(map(int,input().split()))
N = NK[0]
K = NK[1]
result = []

def shift(nList,x):
    tmp = nList.pop(x)
    print(tmp)
    result.append(tmp)

nList = [i+1 for i in range(N)]

while nList:
    K = K % N
    shift(nList,K-1)
    K += 3

print(result)