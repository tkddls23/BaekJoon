# 7568 덩치
from sys import stdin

N = int(stdin.readline())
data = []
result = []

flag = 1
for i in range(N):
    x,y = map(int,input().split())
    data.append((x,y))

for i in range(N):
    flag = 1
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            flag +=1
    result.append(flag)

for d in result:
    print(d,end=" ")
