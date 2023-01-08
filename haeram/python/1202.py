from sys import stdin
import heapq

total_jewels, total_bags = map(int, stdin.readline().split())
jewels = [list(map(int, stdin.readline().split())) for _ in range(total_jewels)]
bags = [int(stdin.readline()) for _ in range(total_bags)]
hq = []

jewels = sorted(jewels, key=lambda x: x[0])
bags = sorted(bags)

ans = 0
cand = []
chk = 0
for bag in bags:
    for jewel in jewels:
        if(chk >= total_jewels):
            break
        if(jewel[0] <= bag):
            heapq.heappush(hq, -jewels[chk][1])
            chk+=1

    if(len(hq)):
        ans += -heapq.heappop(hq)

print(ans)
