from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
idx = [i for i in range(m)]

ans = 0

# 1종류 샀을 때
for i in range(m):
    cnt = 0
    for j in range(n):
        cnt += arr[j][i]

    ans = max(ans, cnt)

# 2종류 샀을 때
cands = combinations(idx, 2)
for cand in cands:
    a, b = cand
    cnt = 0
    for i in range(n):
        cnt += max(arr[i][a], arr[i][b])

    ans = max(ans, cnt)

cands = combinations(idx, 3)
for cand in cands:
    a, b, c = cand
    cnt = 0
    for i in range(n):
        cnt += max(arr[i][a], arr[i][b], arr[i][c])

    ans = max(ans, cnt)

print(ans)
