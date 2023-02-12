from itertools import combinations

def solution(number):
    arr = list(combinations(number, 3))
    
    cnt = 0
    for cand in arr:
        if(sum(cand) == 0):
            cnt += 1
    
    return cnt
