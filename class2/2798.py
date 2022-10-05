# 2798 블랙잭

result = 0

countList = list(map(int,input().split()))
N, M = countList[0], countList[1]
valueList = list(map(int,input().split()))

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp = valueList[i] + valueList[j] + valueList[k]
            if result < tmp <= M:
                result = tmp
print(result)