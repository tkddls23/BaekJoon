from sys import stdin
import math

n, cur_atk = map(int, stdin.readline().split())
cur_hp = 0
ans = 0

for _ in range(n):
    t, a, h = map(int, stdin.readline().split())
    
    if t == 1:
        cnt = math.ceil(h/cur_atk) - 1

        cur_hp -= (a * cnt)

    elif t == 2:
        ans = max(ans, -cur_hp+1)
        cur_atk += a
        cur_hp = min(0, cur_hp+h)

ans = max(ans, -cur_hp+1)
print(ans)
