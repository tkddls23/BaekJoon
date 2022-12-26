# 1018 체스판 다시 칠하기
from sys import stdin

# 행렬 입력
N, M = map(int, stdin.readline().split())
chess = []
result = 65

for _ in range(N):
    chess.append(input())


# 체스판 하나하나씩 B와 W일때를 나눠 DRAW
def isDraw(draw1, draw2):
    for a in range(i, i + 8):
        for b in range(j, j + 8):
            if (a + b) % 2 == 0:
                if chess[a][b] != 'B':
                    draw1 += 1
                if chess[a][b] != 'W':
                    draw2 += 1
            if (a + b) % 2 != 0:
                if chess[a][b] != 'W':
                    draw1 += 1
                if chess[a][b] != 'B':
                    draw2 += 1

    return min(draw1, draw2)


# 8*8 크기의 체스판으로 자른다
for i in range(N - 7):
    for j in range(M - 7):
        draw1 = 0
        draw2 = 0

        result = min(result, isDraw(draw1, draw2))
print(result)
