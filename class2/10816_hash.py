# 10816 숫자 카드2
import sys
N = int(sys.stdin.readline())
cardNum = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
hasCardNum = list(map(int,sys.stdin.readline().split()))

hash = {}
result = []

for i in cardNum:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in hasCardNum:
    if i in hash:
        result.append(hash[i])
    else:
        result.append(0)

print(" ".join(map(str, result)))
