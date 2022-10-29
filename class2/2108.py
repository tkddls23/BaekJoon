from sys import stdin 
import statistics

N = int(stdin.readline())
result = []
for i in range(N):
    result.append(int(stdin.readline()))

result.sort()

print(round(sum(result)/N))
print(result[N//2])

tmp = statistics.mode(result)
count1 = result.count(tmp)
if len(result) != 1:
    result.remove(tmp)

    tmp2 = statistics.mode(result)
    count2 = result.count(tmp2)

    if count1 == count2:
        print(tmp2)
    else:
        print(tmp)
    result.append(tmp)

else:
    print(tmp)
print(max(result)-min(result))