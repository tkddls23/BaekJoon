def solution(t, p):
    cnt = 0
    p_len = len(p)
    
    for i in range(len(t)-p_len+1):
        if(int(t[i:i+p_len]) <= int(p)):
            cnt += 1
            
    return cnt
    