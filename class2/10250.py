# 10250 ACM 호텔
import sys, math

T = int(sys.stdin.readline())
testData = {}
for i in range(T):
    testData[i] = list(map(int, input().split()))

for i in range(T):
    H = testData[i][0]
    W = testData[i][1]
    N = testData[i][2]
    if N%H == 0 :
        floor = H
    else:   
        floor = N%H
    room = math.ceil(N/H)
    print(100*floor + room)