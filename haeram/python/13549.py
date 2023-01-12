from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
dq = deque()
visited = [0]*(100001)
time = [-1]*(100001)

dq.append(n)
visited[n] = 1
time[n] = 0

while dq:
    current_loc = dq.popleft()
    
    if(current_loc*2 <= 100000 and not visited[current_loc*2]): # 순간이동
        dq.appendleft(current_loc*2)
        visited[current_loc*2] = 1
        time[current_loc*2] = time[current_loc]

    if(current_loc+1 <= 100000 and not visited[current_loc+1]): # +1 이동
        dq.append(current_loc+1)
        visited[current_loc+1] = 1
        time[current_loc+1] = time[current_loc]+1
    
    if(current_loc-1 >= 0 and not visited[current_loc-1]): # -1 이동
        dq.append(current_loc-1)
        visited[current_loc-1] = 1
        time[current_loc-1] = time[current_loc]+1

    
print(time[k])
