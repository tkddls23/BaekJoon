#  2609 최대공약수와 최소공배수
import sys
nList = list(map(int,sys.stdin.readline().split()))

a = nList[0]
b = nList[1]

for i in range(1,max(nList)+1):
    if a%i == 0 and b%i == 0:
        result = i

print(result)
print(int(a*b/result))