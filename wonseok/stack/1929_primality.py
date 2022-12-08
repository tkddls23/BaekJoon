# 1929 소수 구하기
import sys

MN = list(map(int,sys.stdin.readline().split()))
m = MN[0]
n = MN[1]

def primality(n):
    i = 2
    if i < 2:
        return False

    while i * i <= n:
        if n % i == 0:
            return False
        i+=1
    return True

for i in range(m,n+1):
        if primality(i):
            print(i)