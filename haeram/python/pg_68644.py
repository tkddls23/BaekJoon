from itertools import combinations

def solution(numbers):
    ans_set = set()
    
    arr = combinations(numbers, 2)
    for i in arr:
        ans_set.add(i[0] + i[1])
        
    ans = sorted(list(ans_set))
    return ans