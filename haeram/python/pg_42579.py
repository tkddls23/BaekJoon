def solution(genres, plays):
    dict = {}
    
    # make dictionary
    for i in range(len(genres)):
        if(genres[i] in dict):
            dict[genres[i]] += plays[i]
        else:
            dict[genres[i]] = plays[i]
        
    dict_arr = sorted(dict.items(), key=lambda x:-x[1])
    
    # make array
    arr = []
    
    for i in range(len(genres)):
        arr.append((genres[i], plays[i], i))
    
    arr.sort(key=lambda x:(x[2]))
    arr.sort(key=lambda x:(x[1]), reverse=True)
    
    # make answer
    ans = []
    for d in dict_arr:
        cnt = 0
        for a in arr:
            if(cnt >= d[1] or cnt >= 2):
                break
            
            if(a[0] == d[0]):
                ans.append(a[2])
                cnt += 1
        
    return ans
    