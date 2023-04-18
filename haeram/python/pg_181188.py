def solution(targets):
    targets.sort(key=lambda x: x[1])
    
    # print(targets)
    
    cur_end = 0
    cnt = 0
    for target in targets:
        start, end = target[0], target[1]
        
        if start >= cur_end:
            # print('end', cur_end, end)
            cur_end = end
            cnt += 1
            
    return cnt