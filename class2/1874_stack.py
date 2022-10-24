# 1874 스택  수열
from sys import stdin

n = int(stdin.readline())
stack = []
result = []
cur = 1
flag = 0

for i in range(n):
    num = int(stdin.readline())
    while cur <= num:
        stack.append(cur)
        result.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in result:
        print(i)
