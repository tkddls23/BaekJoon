# 7662 이중 우선순위 큐
import heapq
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    min_queue = []
    max_queue = []
    # 방문 여부
    visited = [False] * n

    for i in range(n):
        command, num = map(str, stdin.readline().split())
        num = int(num)
        if command == 'I':
            heapq.heappush(min_queue, (num, i))
            heapq.heappush(max_queue, (-num, i))
            # 방문 체크
            visited[i] = True
        if command == 'D' and len(min_queue) != 0:
            if num == 1:
                while max_queue and not visited[max_queue[0][1]]:
                    heapq.heappop(max_queue)
                if max_queue:
                    visited[max_queue[0][1]] = False
                    heapq.heappop(max_queue)
            if num == -1:
                while min_queue and not visited[min_queue[0][1]]:
                    heapq.heappop(min_queue)
                if min_queue:
                    visited[min_queue[0][1]] = False
                    heapq.heappop(min_queue)
    # 정수가 없다면
    if True not in visited:
        print('EMPTY')
    else:
        # 정수가 있다면
        # 연산이 끝난 후 제거 되지 못한 최대 힙과 최소 힙을 팝하여 제거
        while min_queue and not visited[min_queue[0][1]]:
            heapq.heappop(min_queue)
        while max_queue and not visited[max_queue[0][1]]:
            heapq.heappop(max_queue)
        print(-max_queue[0][0], min_queue[0][0])
