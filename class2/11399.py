# 11399 ATM
from sys import stdin 

n = int(stdin.readline())
prev = 0
atm = list(map(int,stdin.readline().split()))
result = []
atm.sort()


def fibo(prev, num):
    tmp = prev + num
    return tmp

for i in atm:
    prev = fibo(prev,i)
    result.append(prev)

print(sum(result))