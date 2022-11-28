# 7662 이중 우선순위 큐
import heapq
from sys import stdin

t = int(stdin.readline())
result = []
for _ in range(t):
    n = int(stdin.readline())
    queue = []
    max_queue = []
    # 정수 여부
    visited = [False] * n

    for i in range(n):
        command, num = input().split(" ")
        num = int(num)
        if command == 'I':
            heapq.heappush(queue, num)
            heapq.heappush(max_queue, (-num, num))
            # 정수 생성
            visited[i] = True
        if command == 'D' and len(queue) != 0:
            if num == 1:
                while max_queue and visited[max_queue[0][1]] == False:
                    heapq.heappop(max_queue)
                if max_queue:
                    visited[max_queue[0][1]] = False
                    heapq.heappop(max_queue)
            if num == -1:
                while queue and visited[queue[0][1]] == False:
                    heapq.heappop(queue)
                if queue:
                    visited[queue[0][1]] = False
                    heapq.heappop(queue)
    if len(queue) == 0:
        result.append('EMPTY')
    else:
        result.append(f'{heapq.heappop(max_queue)[1]} {heapq.heappop(queue)}')
for i in result:
    print(i)