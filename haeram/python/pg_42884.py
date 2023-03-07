def solution(routes):
    routes.sort(key=lambda x: (x[1], x[0]))
    
    cur_end = -30001
    
    ans = 0
    for r in routes:
        if(cur_end < r[0]):
            cur_end = r[1]
            ans += 1
            
    return ans if ans else 1
    