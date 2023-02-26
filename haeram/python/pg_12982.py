def solution(d, budget):
    ans = 0
    sorted_d = sorted(d)
    
    for i in sorted_d:
        if(i <= budget):
            ans += 1
            budget -= i
        else:
            break
    
    return ans