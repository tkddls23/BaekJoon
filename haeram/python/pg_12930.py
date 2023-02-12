def solution(s):
    ans = ''
    words = s.split(' ')
    
    for word in words:
        for i in range(len(word)):
            if(i%2 == 0):
                ans += word[i].upper()
            else:
                ans += word[i].lower()
                
        ans += ' '
            
    return ans[0:-1]