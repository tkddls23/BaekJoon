# 1966 프린터 큐

n = int(input())
first = []
second = []
result = []
dic = {}
for i in range(n):
    first = list(map(int,input().split()))
    second = list(map(int,input().split()))
    wantIndex = first[1]
    wantNum = second[wantIndex]
    cnt = 0
    while second:
        best = max(second)
        num = second.pop(0)
        wantIndex -= 1

        if num == best:
            cnt += 1
            if wantIndex <0:
                result.append(cnt)
                break
        else:
            second.append(num)
            if wantIndex<0:
                wantIndex = len(second) -1

while result:
    print(result.pop(0))
