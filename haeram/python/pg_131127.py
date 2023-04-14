def solution(want, number, discount):    
    want_dict = {}
    window_dict = {}
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    ans = 0
    # window 초기값
    for i in range(10):
        if discount[i] not in window_dict:
            window_dict[discount[i]] = 1
        else:
            window_dict[discount[i]] += 1
        
    if want_dict == window_dict:
        ans += 1
        
    # print(window_dict)
    for i in range(10, len(discount)):
        window_dict[discount[i-10]] -= 1
        
        if discount[i] not in window_dict:
            window_dict[discount[i]] = 1
        else:
            window_dict[discount[i]] += 1

        if window_dict[discount[i-10]] == 0:
            del window_dict[discount[i-10]]
            
        if want_dict == window_dict:
            ans += 1
            
        # print(window_dict)
        
        
    return ans
        
    
        
    