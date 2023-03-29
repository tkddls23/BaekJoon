import math

def solution(n, s):
    if(n > s):
        return [-1]
    
    quot = s//n
    remainder = s%n
    
    arr = [quot for _ in range(n)]
    
    for i in range(1, remainder+1):
        arr[-i] += 1
        
    return arr