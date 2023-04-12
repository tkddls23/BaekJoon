from collections import deque

def solution(board):
    row = len(board)
    col = len(board[0])
    
    visited = [[0]*col for _ in range(row)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    # get start point and goal
    sy, sx = 0, 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                sy, sx = i, j
    
    dq = deque()
    dq.append((sy, sx))
    visited[sy][sx] = 1
    
    # bfs
    while dq:
        ny, nx = dq.popleft()
        
        if board[ny][nx] == 'G':
            return visited[ny][nx] - 1
        
        for i in range(4):
            cy = ny
            cx = nx

            while 1:
                cy += dy[i]
                cx += dx[i]
                
                # 맵 밖으로 나간 경우
                if (cy>=row or cx>=col or cy<0 or cx<0):
                    cy -= dy[i]
                    cx -= dx[i]
                    break
                    
                # 장애물을 만난 경우
                if (board[cy][cx] == 'D'):
                    cy -= dy[i]
                    cx -= dx[i]
                    break        
            
            if not visited[cy][cx]:
                visited[cy][cx] = visited[ny][nx] + 1
                dq.append((cy, cx))

    return -1