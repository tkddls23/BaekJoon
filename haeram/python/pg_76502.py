def solution(s):
    cnt = 0
    
    for i in range(len(s)):
        stk = []
        
        for j in range(len(s)):
            if (s[j] in ['(', '[', '{']):
                stk.append(s[j])

            if(s[j] in [')', ']', '}']):
                if(s[j] == ')'):
                    if(len(stk) == 0 or stk[-1] != '('):
                        stk.append(s[j])
                        break
                    else:
                        stk.pop()
                        
                if(s[j] == ']'):
                    if(len(stk) == 0 or stk[-1] != '['):
                        stk.append(s[j])
                        break
                    else:
                        stk.pop()
            
                if(s[j] == '}'):
                    if(len(stk) == 0 or stk[-1] != '{'):
                        stk.append(s[j])
                        break
                    else:
                        stk.pop()
        
        if(len(stk) == 0):
            cnt += 1
            
        s = s[1:len(s)] + (s[0]) # shift
        
    return cnt
            
    
    