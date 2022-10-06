# 2751 수정렬하기 2
import sys

NList = []
# input()을 쓰면 시간초과가 나오길래 sys.stdin.readline()으로 수정하였다.
# input() 함수의 경우 prompt message를 출력하고 개행 문자(\n)를 삭제한 값을 리턴해서 느리다
N = int(sys.stdin.readline())
for i in range(N):
    NList.append(int(sys.stdin.readline()))

NList.sort()

for i in  range(N):
    print(NList[i])