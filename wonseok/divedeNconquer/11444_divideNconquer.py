# 11444 피보나치 수 6
from sys import stdin


# n번 째 피보나치 수는 행렬 (1 1, 1 0)^n 의 1행 2열 값 (n>=1)

def mul(A, B):
    n = len(A)
    Z = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += A[row][i] * B[i][col]
            Z[row][col] = e % p

    return Z


def square(fib_matrix, n):
    if n == 1:
        return fib_matrix

    tmp = square(fib_matrix, n // 2)
    if n % 2:
        return mul(mul(tmp, tmp), fib_matrix)
    else:
        return mul(tmp, tmp)


n = int(stdin.readline())
p = 1000000007
fib_matrix = [[1, 1], [1, 0]]

print(square(fib_matrix, n)[0][1])

# memoization로 풀었는데 메모리 초과함
# from sys import stdin
#
# n = int(stdin.readline())
# d = [0] * (n + 1)
#
#
# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         d[n] = 1
#         return 1
#     else:
#         if d[n] != 0:
#             return d[n]
#         d[n] = fibo(n - 2) + fibo(n - 1)
#         return d[n]
#
#
# print(fibo(n) % 1000000007)
