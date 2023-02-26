def solution(k, tangerine):
    #1. 개수 세는 딕셔너리 
    #2. value 가장 큰 순서대로 키 값 뽑아내기
    
    dict = {}
    
    for t in tangerine:
        if(t in dict):
            dict[t] += 1
        else:
            dict[t] = 1
    
    sorted_dict = sorted(dict.items(), reverse=True, key=lambda x: x[1])

    cnt = 0
    ans = 0
    for s in sorted_dict:
        ans += 1
        cnt += s[1]
        
        if(cnt >= k):
            return ans
    
    