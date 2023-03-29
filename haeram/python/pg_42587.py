from collections import deque

def solution(priorities, location):
    dq = deque()
    
    for i in range(len(priorities)):
        dq.append([priorities[i], i])
        
    ans = 0
    
    while dq:
        cur = dq.popleft()
        
        if(not dq):
            return ans + 1
        
        if(dq and cur[0] >= max(dq)[0]):
            ans += 1
            
            if(cur[1] == location):
                return ans
            
        else:
            dq.append(cur)
        
    
    
    