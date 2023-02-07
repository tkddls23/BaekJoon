def solution(a, b, n):
    rest = n
    ans = 0
    
    while (rest>=a):
        add_new = rest//a
        ans += (add_new)*b
        rest -= (add_new*a)
        rest += (add_new)*b
        
    return ans
    