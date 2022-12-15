# 1107 리모컨
from sys import stdin

N = int(stdin.readline())
m = int(stdin.readline())
ans = abs(100-N)

if m:
    btn = set(stdin.readline().split())
else:
    btn = set()

for num in range(1000001):
    for i in str(num):
        if i in btn: # 고장난 번호를 포함하는 경우
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
        # min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(num)) + abs(num - N))


print(ans)