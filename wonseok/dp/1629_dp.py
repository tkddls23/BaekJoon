# 1629 곱셈
import math
from sys import stdin

"""
지수 법칙 나머지 분배 법칙을 알아야 풀 수 있음 난 몰라서 틀렸다
A^m+n = A^m x A^n
(AxB)%C = (A%C) *(B%C) % C
"""
a,b,c = map(int,stdin.readline().split())

def dp(n):
    if n == 1:
        return a%c
    else:
        tmp = dp(n//2)
        if n % 2 ==0:
            return (tmp * tmp) % c
        else:
            return (tmp  * tmp *a) %c

print(dp(b))