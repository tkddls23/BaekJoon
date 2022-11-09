# 10989 수 정렬하기 3
import sys

N = int(sys.stdin.readline())

nList = [0] * 10001

for i in range(N):
    nList[int(sys.stdin.readline())] += 1

for i in range(10001):
    if nList[i] != 0:
        for j in range(nList[i]):
            print(i)
