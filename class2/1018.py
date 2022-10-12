# 1018 체스판 다시 칠하기
import sys

NM = list(map(int,sys.stdin.readline().split()))

N = NM[0]
M = NM[1]

chessDic = {}

for i in range(N):
    chessDic[i] = input()

for i in range(N%8):

    print(chessDic[i])

def retrieveColorCount():
    return True