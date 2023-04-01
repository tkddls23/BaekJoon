def solution(cards):
    visited = []
    cands = []
    
    for i in range(len(cards)):
        if(i == 1 and len(visited) == len(cards)):
            return 0
            
        if(i in visited):
            continue
            
        cnt = 0
        idx = i
        while 1:
            if(idx in visited):
                cands.append(cnt)
                break
            
            visited.append(idx)
            cnt += 1
            if(idx >= len(cards)):
                break
            idx = cards[idx]-1
                
    cands.sort(reverse=True)
    return cands[0] * cands[1]
    
