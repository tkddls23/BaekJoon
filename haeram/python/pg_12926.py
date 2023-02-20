def solution(s, n):
    res = ''
    s_list = list(s)
    
    for alp in s_list:
        if(alp.isupper()):
            converted = chr((ord(alp)+n - ord('A'))%26 + ord('A'))
            res += converted
        elif(alp.islower()):
            converted = chr((ord(alp)+n - ord('a'))%26 + ord('a'))
            res += converted
        else:
            res += alp
    
    return res