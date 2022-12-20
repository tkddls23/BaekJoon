# 5525 IOIOI
from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().rstrip()

answer, i, count = 0, 0, 0

# IOI가 몇 번 연속되는지 갯수만 찾아서 체크
while i < (m - 1):
    if s[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == n:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0
print(answer)