def solution(babbling):
    pron = ["aya", "ye", "woo", "ma"]
    
    ans = 0
    for cand in babbling:
        flag = True
        for p in pron:
            # 2개 연속 발음인 경우 제외
            if p*2 in cand:
                flag = False
                break
                
            cand = cand.replace(p, ' ')
            
        if flag and cand.strip() == '':
            ans += 1
            
    return ans
            