import heapq

# heappush() : o(logN) 
def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap)

    cnt = 0
    while True:
        t = heapq.heappop(heap)

        if t >= K:
            return cnt

        if not heap:
            return -1

        cnt += 1
        t2 = heapq.heappop(heap)

        new_t = t + (t2 * 2)
        heapq.heappush(heap, new_t)

