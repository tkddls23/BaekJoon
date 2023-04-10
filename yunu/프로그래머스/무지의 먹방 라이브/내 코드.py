from heapq import heappush, heappop, heapify

def solution(food_times, k):
    
    food_times = [[time, i] for i, time in enumerate(food_times)]
    heapify(food_times)
    
    n = len(food_times)
    [time, i] = heappop(food_times)
    minTime = time
    finished = [False for _ in range(n)]
    while k >= time * n:
        if not food_times:
            return -1
        k -= time * n
        n -= 1
        finished[i] = True
        [nextTime, j] = heappop(food_times)
        time = nextTime - minTime
        minTime = nextTime
        i = j
    
    k %= n
    for i, flag in enumerate(finished):
        if flag:
            continue
        else:
            if k == 0:
                return i + 1
            k -= 1
        
    return -1