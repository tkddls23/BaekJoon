# 2798 블랙잭

from itertools import combinations

result = 0

countList = list(map(int,input().split()))
N, M = countList[0], countList[1]
valueList = list(map(int,input().split()))

for cars in combinations(valueList, 3):
    tmp = sum(cars)
    if result < tmp <= M:
        result = tmp
print(result)