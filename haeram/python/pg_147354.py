def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    # make hash values
    cand = []
    for row in range(row_begin, row_end+1):
        temp = 0
        target_arr = data[row-1]
        
        for t in target_arr:
            temp += t % row
            
        cand.append(temp)
        
    # get answer
    ans = 0
    for i in range(len(cand)):
        ans ^= cand[i]
        
    return ans