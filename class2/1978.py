# 1978 소수 판별

N = int(input())
NList = list(map(int, input().split()))
result = 0

def primality(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i+=1
    return True

for i in range(N):
    if  NList[i] != 1 and primality(NList[i]) == True:
        result +=1

print(result)


