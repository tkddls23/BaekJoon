def solution(today, terms, privacies):
    y, m, d = map(int, today.split('.'))
    term_dict = {}
    for t in terms:
        key, val = t.split()
        term_dict[key] = int(val)
    
    ans = []
    for i in range(len(privacies)):
        start, term = privacies[i].split()
        sy, sm, sd = map(int, start.split('.'))
        
        year_diff = y-sy
        month_diff = m-sm
        day_diff = d-sd
        
        diff = day_diff + month_diff*28 + year_diff*12*28
        
        
        if diff // 28 >= term_dict[term]:
            ans.append(i+1)
            
    return ans
    