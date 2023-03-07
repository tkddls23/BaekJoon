import heapq

def solution(operations):
    max_hq = []
    min_hq = []
    hq_size = 0
    available = []
    
    heapq.heapify(max_hq)
    heapq.heapify(min_hq)
    
    for o in operations:
        operator, num = o.split()
        num = int(num)
        
        if(operator == 'I'):
            heapq.heappush(min_hq, num)
            heapq.heappush(max_hq, -num)
            available.append(num)
            hq_size += 1
            
        elif(operator == 'D'):
            if(hq_size <= 0):
                continue
                
            if(num == -1):
                popped = heapq.heappop(min_hq)
                hq_size -= 1
                if(popped in available):
                    available.remove(popped)
            elif(num == 1):
                popped = -heapq.heappop(max_hq)
                hq_size -= 1
                if(popped in available):
                    available.remove(popped)
    
    if(hq_size <= 1):
        return [0, 0]
    else:
        return [max(available), min(available)]
                
