def solution(clothes):
    dict = {}
    
    for cloth in clothes:
        if(cloth[1] in dict):
            dict[cloth[1]].append(cloth[0])
        else:
            dict[cloth[1]] = [cloth[0]]
    
    ans = 1
    for keys in dict:
        ans *= len(dict[keys])+1

    return ans-1