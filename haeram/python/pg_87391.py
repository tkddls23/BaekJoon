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
# def solution(n, m, x, y, queries):
#     queries.reverse()
#     sx = x
#     sy = y
#     ex = x
#     ey = y
    
#     for i in range(len(queries)):
#         op, dx = queries[i][0], queries[i][1]
        
#         if op == 0:
#             ex = min(m-1, nx+dx)
#             nx = ex
#         if op == 1:
#             ex = max(0, nx-dx)
#             nx = ex
#         if op == 2:
#             ey = min(n-1, ny+dx)
#             ny = ey
#         if op == 3:
#             ey = max(0, ny-dx)
#             ny = ey
            
#     # 마지막 경우 계산
#     ans = (n - nx + 1) * (m - ny + 1)
#     print(nx, ny)
#     return ans
        
        
# # print(solution(2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]])) # 4
# print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]])) # 2

