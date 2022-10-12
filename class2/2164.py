# 2164 카드2
import sys, math

N = int(sys.stdin.readline())
xList = [i*2 for i in range(1,(N//2)+1)]

r = math.ceil(N/2)
if N!= 1:
    for i in range(r):
        tmp = xList.pop(0)
        xList.append(tmp)

if N==1:
    print("1")
elif N<=3:
    print("2")
else:
    xList.pop(0)
    print(xList[0])

