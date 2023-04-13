import heapq

def solution(scoville, K):    
    heapq.heapify(scoville)
    
    cnt = 0
    while 1:
        if cnt > 1e9:
            return -1
        
        v1 = heapq.heappop(scoville)
        if v1 >= K:
            return cnt
        
        if not scoville:
            return -1
        
        v2 = heapq.heappop(scoville)
        
        mixed = v1 + v2*2
        
        heapq.heappush(scoville, mixed)
        cnt += 1
        
    
    