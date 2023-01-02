# 9663 N-Queen
from sys import stdin

n = int(stdin.readline())
row = [0] * n
result = 0


# 상하 대각선(위에서부터 체스를 채우니 위에 대각선만 확인) 체크
def check(n):
    for i in range(n):
        if (row[n] == row[i]) or (n - i == abs(row[n] - row[i])):
            return False
    return True


def n_queens(r):
    global result
    if r == n:
        result += 1
        return

    for i in range(n):
        # [x, i]에 놓는다
        row[r] = i
        if check(r):
            n_queens(r + 1)


n_queens(0)
print(result)
