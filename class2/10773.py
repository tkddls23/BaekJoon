# 10773 제로
import sys

K = int(input())
l = []
result = 0
x = 0
for i in range(K):
    l.append(int(sys.stdin.readline()))

while l:
    tmp = l.pop()
    if tmp == 0:
        x +=1
        if l[-1] != 0:
            for i in range(x):
                l.pop()
            x = 0
    else:
        result += tmp

print(result)