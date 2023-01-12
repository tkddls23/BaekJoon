from sys import stdin
from queue import PriorityQueue

n = int(stdin.readline())
arr = []
pq = PriorityQueue()

for _ in range(n):
    d, c = map(int, stdin.readline().split())

    arr.append((d, c))

arr = sorted(arr, key=lambda x:(x[0], x[1]))

ans = 0
for day in range(n):
    ans += arr[day][1]
    pq.put(arr[day][1])

    if(pq.qsize() > arr[day][0]):
        ans -= pq.get()
    
print(ans)