def solution(keymap, targets):
    dict = {}

    for keys in keymap:
        for i in range(len(keys)):
            if keys[i] not in dict:
                dict[keys[i]] = i+1
            else:
                dict[keys[i]] = min(dict[keys[i]], i+1)
    
    ans = []
    for target in targets:
        cnt = 0
        valid = True
        
        for t in target:
            if t not in dict:
                valid = False
                ans.append(-1)
                break
            
            else:
                cnt += dict[t]
                
        if valid:
            ans.append(cnt)
            
    return ans