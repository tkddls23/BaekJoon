from sys import stdin

n, c = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

freqMap = {}

for it in arr:
    try:
        freqMap[it]+=1
    except:
        freqMap[it] = 1

freqMap = sorted(freqMap.items(), key=lambda x: x[1], reverse=True)

for it in freqMap:
    for _ in range(it[1]):
        print(it[0], end=' ')