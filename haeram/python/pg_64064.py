from itertools import permutations

def is_same(s1, s2):    
    if(len(s1) != len(s2)):
        return False
    
    for i in range(len(s1)):
        if(s2[i] == '*'):
            continue
            
        if(s1[i] != s2[i]):
            return False
        
    return True
    

def solution(user_id, banned_id):
    ans = set()
    temp = list(permutations(user_id, len(banned_id)))

    for cand in temp:
        banned = []
        for i in range(len(cand)):
            if(is_same(cand[i], banned_id[i])):
                banned.append(cand[i])
                
        if(len(banned) == len(cand)):
            banned.sort()
            ans.add("".join(banned))
            
    return len(ans)
