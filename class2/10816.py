# 10816 숫자 카드2
import sys
N = int(sys.stdin.readline())
cardNum = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
hasCardNum = list(map(int,sys.stdin.readline().split()))

cardSet = set(cardNum)
hasCardSet = set(hasCardNum)
difference = hasCardSet - cardSet
result = []
resultList = result.append


for i in hasCardNum:
    if i in difference:
        resultList(0)
    else:
        resultList(cardNum.count(i))

print(result)