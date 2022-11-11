# 11650 좌표 정렬하기
import sys
nDic = {}
key = []
N = int(sys.stdin.readline())
for i in range(N):
    nDic[i] = list(map(int,sys.stdin.readline().split()))

sortedDic = sorted(nDic.items(), key = lambda item: item[1])
for i in sortedDic:
    joinedStr = ' '.join([str(n) for n in i[1]])
    print(joinedStr)
