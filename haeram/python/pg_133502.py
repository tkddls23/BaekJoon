def solution(ingredient):
    stk = []
    
    ans = 0
    for i in ingredient:
        stk.append(i)
        
        if len(stk) < 4:
            continue
            
        if stk[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stk.pop()
            
            ans += 1
            
    return ans