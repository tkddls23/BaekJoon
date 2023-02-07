# 풀이 1 : 시간 초과 (수의 범위가 10**6)
def getLCM(n, m):
    small = min(n, m)
    big = max(n, m)
    
    times = 1    
    while True:
        if(big*times % small == 0):
            return big*times
        
def getGCD(n, m):
    small = min(n, m)
    big = max(n, m)
    
    divisors = []
    for i in range(small, 0, -1):
        if(small % i == 0):
            divisors.append(i)
    
    for i in divisors:
        if(big % i == 0):
            return i
    

def solution(n, m):
    gcd = getGCD(n, m)
    lcm = getLCM(n, m)
    
    return [gcd, lcm]


# 풀이 2 : O(N)으로 변경
def getLCM(n, m):
    small = min(n, m)
    big = max(n, m)
    
    for i in range(big, (small*big)+1):
        if(i%small == 0 and i%big == 0):
            return i
        
def getGCD(n, m):
    small = min(n, m)
    big = max(n, m)
    
    for i in range(small, 0, -1):
        if(small%i == 0 and big%i == 0):
            return i
    

def solution(n, m):
    gcd = getGCD(n, m)
    lcm = getLCM(n, m)
    
    return [gcd, lcm]



# 풀이 3 : 유클리드 호제법 이용
def getGCD(n, m):
    small = min(n, m)
    big = max(n, m)

    while(big):
        small, big = big, small%big

    return small
    
def getLCM(n, m):
    res = (n*m) // getGCD(n, m)
    return res


def solution(n, m):
    gcd = getGCD(n, m)
    lcm = getLCM(n, m)

    return [gcd, lcm]