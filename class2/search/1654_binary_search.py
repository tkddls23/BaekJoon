# 1654 랜선 자르기
from sys import stdin
KN = list(map(int,stdin.readline().split()))
k = KN[0]
n = KN[1]
lan = []
result = 0
start = 1

for i in range(k):
    lan.append(int(stdin.readline()))

end = max(lan)

while (start <= end):
    mid = (start + end) // 2
    result = 0
    for i in range(k):
        result += lan[i] // mid
    if result >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)


