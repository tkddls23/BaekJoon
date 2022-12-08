# 1620 포켓몬
from sys import stdin 

n,m = map(int,stdin.readline().split())
dic = {}
que = []

for i in range(n):
    tmp = input().rstrip()
    dic[i+1] = tmp
    dic[tmp] = i+1


for j in range(m):
    que.append(input())

for k in que:
    if k.isdigit():
        print(dic[int(k)])
    else:
        print(dic[k])