# 1931 회의실 배정
from sys import stdin 

n = int(stdin.readline())
arr = []
cnt = 1

for i in range(n):
    a, b = map(int,stdin.readline().split())
    arr.append([a,b])

sortArr = sorted(arr, key=lambda x: (x[1], x[0]))

end = sortArr[0][1]
for i in range(1,n):
    if sortArr[i][0] >= end:
        cnt += 1
        end = sortArr[i][1]

print(cnt)
