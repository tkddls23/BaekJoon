# def count_unique_combinations(n, k):
#     dp = [[0] * (k + 1) for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for j in range(1, min(k, i) + 1):
#             if j == 1 or i == j:
#                 dp[i][j] = 1
#             else:
#                 dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
#     return dp[n][k]

# print(count_unique_combinations(9, 3))


# 1.
# def solution(n):
#     if(n < 3):
#         return -1

#     if(n == 3):
#         return 1

#     if(n%5 == 0):
#         return n//5

#     box_3 = 0
#     while n>0:
#         n -= 3
#         box_3 += 1
        
#         if(n%5 == 0):
#             return (n//5 + box_3)

#     return -1


# 2. 
# for i in range(1, len(s)//2 + 1):
#         if(len(s)%i == 0):
#             cand = s[0:i]
#             flag = True

#             for j in range(i, len(s), i):
#                 if(s[j: j+i] != cand):
#                     flag = False
#                     break

                
#             if(flag):
#                 return i

#     return len(s)


# 3. 
# def solution(n, k):
#     if(k == 0):
#         return 0
#     if(n < k*(k+1)):
#         return 0

#     if(k == 1):
#         return 1


#     dp = [[0]*(k+1) for _ in range(n+1)]
#     for i in range(n+1):
#         dp[i][0] = 0
#         dp[i][1] = 1
    
#     for i in range(1, n+1):
#         for j in range(1, k+1):
#             if(i >= j):
#                 dp[i][j] = (dp[i-1][j-1]%1000000007 + dp[i-2][k-1]%1000000007)%1000000007
    
#     return dp[n][k]%1000000007

str = 'abcdef'

print(str[0:4])