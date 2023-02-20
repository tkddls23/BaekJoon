# f(x) = f(x/2) (x가 짝수)
# f(x) = f(x-1) + 1 (x가 홀수)

# 당연히 시간 초과가 난다. n이 10억까지기 때문에, O(N)은 안된다.
def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    
    for i in range(2, n+1):
        if(i%2 == 0):
            dp[i] = dp[int(i/2)]
        else:
            dp[i] = dp[i-1]+1
    
    return dp[n]


# n에서부터 내려가면 된다.
def solution(n):
    ans = 0
    while n > 1:
        if(n%2 == 0):
            n /= 2
        else:
            ans += 1
            n -= 1
            n /= 2
    
    return ans+1 #마지막에 0 -> 1 로 가는 경우인 1을 더해준다.


# 이진수를 이용한 풀이 -> 결국엔 홀수 개수를 세는 것이다.
def solution(n):
    return bin(n).count('1')