import heapq

def solution(n, works):
    if(sum(works) < n):
        return 0
    
    hq = []
    for w in works:
        heapq.heappush(hq, -w)
    
    for i in range(n):
        if hq:
            temp = -heapq.heappop(hq)
            heapq.heappush(hq, -(temp-1))
    
    ans = 0
    while hq:
        ans += (heapq.heappop(hq) ** 2)
        
    
    return ans