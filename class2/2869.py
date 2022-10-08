# 2869 달팽이는 올라가고 싶다
import sys, math
numList = list(map(int,sys.stdin.readline().split()))
A = numList[0]
B = numList[1]
V = numList[2]

tmp = V - A
exp = A - B

test1 = tmp/exp
test2 = math.ceil(test1)

if test1 > 0 :
    if test1 <= 1:
        print("2")
    else:
        print(test2 + 1)
else:
    print("1")
