# 11651 - 좌표 정렬하기
import sys

N = int(sys.stdin.readline())
coordinate = []

for i in range(N):
    coordinate.append(list(map(int,sys.stdin.readline().split())))

sortedCoordinate = sorted(coordinate, key = lambda item: (item[1],item[0]))

for i in sortedCoordinate:
    joinedStr = ' '.join([str(n) for n in i])
    print(joinedStr)