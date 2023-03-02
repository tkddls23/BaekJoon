# 4344 평균은 넘겠지
from sys import stdin

c = int(stdin.readline())

for _ in range(c):
    cnt = 0
    arr = list(map(int,stdin.readline().split()))
    n = arr.pop(0)
    avg = int(sum(arr)/n)
    for i in arr:
        if i > avg:
            cnt += 1
    print(f'{(cnt/n*100):.3f}%')