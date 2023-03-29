def solution(s):
    arr = []
    dict = {}
    for i in range(len(s)):
        if(s[i] not in dict):
            arr.append(-1)
            dict[s[i]] = i
        else:
            arr.append(i - dict[s[i]])
            dict[s[i]] = i
            
    return arr