def getDivisors(s, e):
    arr = [0] * (e+1)
    
    for n in range(s, e+1):
        chk = 0
        for it in range(1, n+1):
            if(n % it == 0):
                chk += 1
        
        arr[n] = chk
        
    return arr


def solution(left, right):
    ans = 0
    divisors = getDivisors(left, right)
    
    for i in range(left, right+1):
        if(divisors[i]%2 == 0): #even
            ans += i
        else: #odd
            ans -= i

    return ans
            


# 제곱수는 약수가 홀수개 라는 성질을 이용한 풀이입니다
def solution2(left, right):
    answer = 0

    for i in range(left, right+1):
        if( int(i**0.5) == i**0.5 ): #제곱수인 경우 => 약수가 홀수개!
            answer -= i
        else:
            answer += i

    return answer