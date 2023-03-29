def k_base(num, k):
    temp = num
    
    converted = ''
    while temp >= k:
        modular = temp % k
        temp = temp // k
        
        converted = str(modular) + converted
        
    res = str(temp) + converted
    return res
        
def is_prime(num):
    if(num == 1):
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if(num % i == 0):
            return False
        
    return True
        
    
def solution(n, k):
    con = k_base(n, k)
    con_arr = con.split('0')
    
    ans = 0
    for c in con_arr:
        if(not len(c)):
            continue
        
        if(is_prime(int(c))):
            ans += 1
            
    return ans
    