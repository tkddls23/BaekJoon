# 9465 스티커
from sys import stdin

t = int(stdin.readline())

for i in range(t):
    col = int(stdin.readline())
    matrix = [list(map(int, stdin.readline().split())) for _ in range(2)]

    for j in range(1,col):
        if j == 1:
            matrix[0][j] += matrix[1][j-1]
            matrix[1][j] += matrix[0][j-1]
        else:
            matrix[0][j] += max(matrix[1][j - 1], matrix[1][j - 2])
            matrix[1][j] += max(matrix[0][j - 1], matrix[0][j - 2])

    print(max(matrix[0][col - 1], matrix[1][col - 1]))
'''
첫 시도

up = 0
down = 0

for i in range(t):
    matrix = [list(map(int, stdin.readline().split())) for _ in range(2)]
    total = sum([sum(i) for i in matrix])
    print(total)
    for i in range(2):
        if i == 0:
            up = sum(matrix[i][0::2])
            print(up)
        if i == 1:
            down = sum(matrix[i][1::2])
            print(down)
    first = up+down
    print(max(first,total-first))
'''