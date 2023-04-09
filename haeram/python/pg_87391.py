# 시간초과 난 코드
# from collections import deque

# def solution(n, m, x, y, queries):
#     queries.reverse()
    
#     dq = deque()
#     dq.append((x, y)) # 도착지점
    
#     for i in range(len(queries)):
#         cur_dq = deque()
        
#         while dq:
#             ny, nx = dq.popleft()
            
#             if(queries[i][0] == 0): # x-
#                 if(nx == 0):
#                     for j in range(0, min(m-1, queries[i][1]) + 1):
#                         cur_dq.append((ny, j))
#                 else:
#                     cur_dq.append((ny, min(m-1, nx + queries[i][1])))
#             elif(queries[i][0] == 1): # x+
#                 if(nx == m-1):
#                     for j in range(max(0, nx - queries[i][1]), nx + 1):
#                         cur_dq.append((ny, j))
#                 else:
#                     cur_dq.append((ny, max(0, nx - queries[i][1])))
#             elif(queries[i][0] == 2): # y-
#                 if(ny == 0):
#                     for j in range(0, min(n-1, queries[i][1]) + 1):
#                         cur_dq.append((j, nx))
#                 else:
#                     cur_dq.append((min(n-1, ny + queries[i][1]), nx))
#             elif(queries[i][0] == 3): # y+
#                 if(ny == n-1):
#                     for j in range(max(0, ny - queries[i][1]), ny + 1):
#                         cur_dq.append((j, nx))
#                 else:
#                     cur_dq.append((max(0, ny - queries[i][1]), nx))
#         dq = cur_dq
    
#     ans_set = set(dq)
    
#     return len(ans_set)

# ----------------------------------------------------------------------------- #


