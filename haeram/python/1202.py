from sys import stdin
import heapq

total_jewels, total_bags = map(int, stdin.readline().split())
jewels = [list(map(int, stdin.readline().split())) for _ in range(total_jewels)]
bags = [int(stdin.readline()) for _ in range(total_bags)]

jewels.sort()
bags.sort()

ans = 0
hq = []
for bag in bags:
    while (jewels and bag>=jewels[0][0]):
        heapq.heappush(hq, -heapq.heappop(jewels)[1])

    if hq:
        ans += -heapq.heappop(hq)
    
print(ans)
