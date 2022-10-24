# 7568 덩치
from sys import stdin

<<<<<<< HEAD

N = int(stdin.readline())
xy = []
dic = {}
=======
N = int(stdin.readline())
data = []
>>>>>>> c067101b1b85fa7f3760e68d870e3f870169d274
result = []

flag = 1
for i in range(N):
<<<<<<< HEAD
    xy = list(map(int,stdin.readline().split()))
    dic[xy[0]] = xy[1]


for i in dic:
    for j in dic:
        if j>i and dic[j] >dic[i]:
            flag +=1
    result.append(flag)
    flag = 1

print(' '.join([str(n) for n in result]))
=======
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
>>>>>>> c067101b1b85fa7f3760e68d870e3f870169d274
