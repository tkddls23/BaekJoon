# 1920 수 찾기
import sys
N = int(sys.stdin.readline())
nList = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
mList = list(map(int,sys.stdin.readline().split()))


nSet = set(nList)
mSet = set(mList)

x = nSet.intersection(mSet)
y = nSet.difference(mSet)


for i in mList:
    if i in x:
        print("1")
    else:
        print("0")