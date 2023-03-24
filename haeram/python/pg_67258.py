def solution(gems):
    # 모든 보석들을 가지고 있는 set 생성
    ref = set(gems)
    ref_len = len(ref)
    
    ans_len = 100001
    ans = []
    
    cand = {}
    start = 0
    end = 0
    
    while(end < len(gems) and start <= end):
        if(gems[end] not in cand):
            cand[gems[end]] = 1
        else:
            cand[gems[end]] += 1
            
        end += 1
        
        if(len(cand) == ref_len):
            while(start < end):
                if(cand[gems[start]] > 1):
                    cand[gems[start]] -= 1
                    start += 1
                
                elif(cand[gems[start]] == 1 and ans_len > end-start):
                    ans_len = end-start
                    ans = [start+1, end]
                    continue
                        
                else:
                    break
                    
    return ans
    
    