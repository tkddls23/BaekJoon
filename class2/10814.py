# 10814 나이순 정렬
import sys
N = int(sys.stdin.readline())
nDic = {}
for i in range(N):
    nDic[i] = input().split()
    nDic[i][0] = int(nDic[i][0])
sortedDic = sorted(nDic.items(), key = lambda item: item[1][0])

for i in sortedDic:
    print(' '.join(str(n) for n in i[1]))

