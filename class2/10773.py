# 10773 제로
import sys

K = int(input())
l = []
result = 0
x = 0
for i in range(K):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        l.pop()
    else:
        l.append(tmp)
    
print(sum(l))
