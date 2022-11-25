# 1074 Z
from sys import stdin

n, r, c = map(int,stdin.readline().split())

cnt = 0
while n != 0:
    n -= 1
    size = 2**n

    if r < size and c < size:
        cnt += 0
    elif r < size and c >= size:
        cnt += size**2
        c -= size
    elif r >= size and c < size:
        cnt += (size**2) * 2
        r -= size
    else:
        cnt += (size ** 2) * 3
        r -= size
        c -= size
print(cnt)