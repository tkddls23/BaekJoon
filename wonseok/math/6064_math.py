# 6064 카잉 달력
from sys import stdin

t = int(input())

# x에  m을 더해주고 y를 뺀값이 n에 나누어떨어지면 정답
for i in range(t):
    m, n, x, y = map(int, input().split())
    while x <= m * n:
        if (x - y) % n == 0:
            break
        x += m
    print(x)