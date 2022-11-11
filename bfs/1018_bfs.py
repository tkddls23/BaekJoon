# 1018 체스판 다시 칠하기
import sys

NM = list(map(int,sys.stdin.readline().split()))

N = NM[0]
M = NM[1]

chess = []
result = []
def isDraw(chess,draw1,draw2,result):
    for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if chess[a][b] != 'B':
                        draw1 += 1
                    if chess[a][b] != 'W':
                        draw2 += 1
                else:
                    if chess[a][b] != 'W':
                        draw1 += 1
                    if chess[a][b] != 'B':
                        draw2 += 1
    result.append(draw1)
    result.append(draw2)
    return result

for _ in range(N):
    chess.append(input())

for i in range(N-7):
    for j in range(M-7):
        draw1 = 0
        draw2 = 0

        isDraw(chess,draw1,draw2,result)
print(min(result))