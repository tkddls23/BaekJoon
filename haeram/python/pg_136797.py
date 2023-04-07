# 시간 초과

# from collections import deque

# def calc(origin, next):
#     cost_map = [
#         [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
#         [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
#         [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
#         [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
#         [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
#         [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
#         [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
#         [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
#         [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
#         [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]
#     ]
    
#     return cost_map[origin][next]
    

# def solution(numbers):
#     dq = deque()
#     dq.append((4, 6, 0, 0)) # left, right, depth, psum
    
#     length = len(numbers)
#     ans = 1e9
    
#     while dq:
#         left, right, depth, psum = dq.popleft()
        
#         if(depth == length):
#             ans = min(ans, psum)
#             continue
            
#         # 왼손으로 누르는 경우
#         to_left = calc(left, int(numbers[depth]))
#         if(psum+to_left < ans and right != int(numbers[depth])):
#             dq.append((int(numbers[depth]), right, depth+1, psum+to_left))
        
#         # 오른손으로 누르는 경우
#         to_right = calc(right, int(numbers[depth]))
#         if(psum+to_right < ans and left != int(numbers[depth])):
#             dq.append((left, int(numbers[depth]), depth+1, psum+to_right))
    
#     return ans
        

# ----------------------------------------------------------------------------------- #

from collections import deque

def calc(origin, next):
    cost_map = [
        [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]
    ]
    
    return cost_map[origin][next]
    

def solution(numbers):    
    dict = {(4, 6): 0} # (left, right) : weight
    
    for n in numbers:
        n = int(n)
        temp_dict = {}
        
        for (left, right), weight in dict.items():
            if(left == n): # 왼손이랑 동일한 숫자인 경우 -> 왼손으로 누름
                if((n, right) not in temp_dict or temp_dict[(n, right)] > weight+1):
                    temp_dict[(n, right)] = weight+1
            elif(right == n): # 오른손이랑 동일한 숫자인 경우 -> 오른손으로 누름
                if((left, n) not in temp_dict or temp_dict[(left, n)] > weight+1):
                    temp_dict[(left, n)] = weight+1
            else:
                cost_left = calc(left, n)
                cost_right = calc(right, n)
                if((n, right) not in temp_dict or temp_dict[(n, right)] > weight+cost_left): # 왼손으로 누르는 경우의 수
                    
                    temp_dict[(n, right)] = weight + cost_left
                if((left, n) not in temp_dict or temp_dict[(left, n)] > weight+cost_right): # 오른손으로 누르는 경우의 수
                    
                    temp_dict[(left, n)] = weight + cost_right
                    
        dict = temp_dict
        
    return min(dict.values())
