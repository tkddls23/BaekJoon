# 7568 덩치
from sys import stdin


N = int(stdin.readline())
xy = []
dic = {}
result = []

flag = 1
for i in range(N):
    xy = list(map(int,stdin.readline().split()))
    dic[xy[0]] = xy[1]


for i in dic:
    for j in dic:
        if j>i and dic[j] >dic[i]:
            flag +=1
    result.append(flag)
    flag = 1

print(' '.join([str(n) for n in result]))
