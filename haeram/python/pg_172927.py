def solution(picks, minerals):
    total_picks = sum(picks)
    groupings = []
    bp = 0
    
    end = min(total_picks, len(minerals)//5)
    for i in range(end):
        temp = {
            'diamond': 0, 
            'iron': 0,
            'stone': 0
        }
        for j in range(5*i, 5*i+5):
            temp[minerals[j]] += 1
            
        groupings.append(temp)
        bp = j
            
    if total_picks > end:
        temp = {
            'diamond': 0, 
            'iron': 0,
            'stone': 0
        }
        
        for i in range(bp+1, len(minerals)):            
            temp[minerals[i]] += 1

        groupings.append(temp)
    
    groupings.sort(key=lambda x: (-x['diamond'], -x['iron'], -x['stone']))
    # print(groupings)
    
    ans = 0    
    for group in groupings:
        if sum(picks) == 0:
            break
            
        # diamond pick
        if picks[0]:
            ans += (1*group['diamond'] + 1*group['iron'] + 1*group['stone'])
            picks[0] -= 1
            continue
           
        if picks[1]:
            ans += (5*group['diamond'] + 1*group['iron'] + 1*group['stone'])
            picks[1] -= 1
            continue
        
        if picks[2]:
            ans += (25*group['diamond'] + 5*group['iron'] + 1*group['stone'])
            picks[2] -= 1
            continue
            
    
    return ans
    