# 1463 1로만들기
from sys import stdin 

x = int(stdin.readline())
d = [0 for _ in range(x+1)]

for i in range(2,x+1):

    d[i] = d[i-1] +1

    if i%3 ==0:
        d[i] = min(d[i],d[i//3]+1)
    if i%2==0:
        d[i] = min(d[i],d[i//2]+1)

print(d[x])
    


    