from sys import stdin
from queue import PriorityQueue

arr = []
pq = PriorityQueue()
n = int(stdin.readline())

#get input
for i in range(n):
    p, d = map(int, stdin.readline().split())
    arr.append((p, d))

#1번째, 그 다음은 0번째 요소 기준으로 정렬
sorted_arr = sorted(arr, key=lambda x:(x[1], x[0]))

#priority queue에 값들 설정
for i in range(n):
    pq.put(sorted_arr[i][0])
    if(pq.qsize() > sorted_arr[i][1]):
        pq.get()

#calculate
ans = 0
while pq.qsize():
    temp = pq.get()
    ans += temp

print(ans)