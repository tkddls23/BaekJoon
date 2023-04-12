def solution(msg):
    dict = {}
    
    for i in range(26):
        dict[chr(65+i)] = i+1
        
    ans = []
    idx = 1
    cand = msg[0]
    cur_value = 27
    while idx < len(msg):
        prev = cand
        cand += msg[idx]
        
        # 없어서 사전에 추가하는 경우
        if(cand not in dict):
            ans.append(dict[prev])
            
            dict[cand] = cur_value
            cur_value += 1
            
            cand = msg[idx]
            idx += 1
            
        # 있는 경우
        else:
            idx += 1
    
    ans.append(dict[cand])
        
    return ans