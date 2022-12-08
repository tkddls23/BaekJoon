# 4673 셀프 넘버
from sys import stdin

numSet = set(range(1,10001))
notSelfNumSet = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    notSelfNumSet.add(i)

selfNumSet = sorted(numSet - notSelfNumSet)

for i in selfNumSet:
    print(i)