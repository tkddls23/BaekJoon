from sys import stdin

str = stdin.readline().rstrip()
cand = stdin.readline().rstrip()

str_len = len(str)
cand_len = len(cand)

ans = 0
idx = 0
while idx < str_len:
    if(str[idx : idx+cand_len] == cand):
        ans += 1
        idx += cand_len
    else:
        idx += 1

print(ans)


# 다른 풀이
from sys import stdin

str = stdin.readline().rstrip()
cand = stdin.readline().rstrip()

str_len = len(str)
cand_len = len(cand)

print(len(str.split(cand)) - 1)
