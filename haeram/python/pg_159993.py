from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    # find start point
    sy, sx = 0, 0
    ey, ex = 0, 0
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'S':
                sy, sx = i, j
                
            if maps[i][j] == 'E':
                ey, ex = i, j
            
                
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    visited = [[0]*col for _ in range(row)]
    
    dq = deque()
    dq.append((sy, sx))
    visited[sy][sx] = 1
    
    lever = False
    while dq:
        y, x = dq.popleft()
        
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            
            if ny<0 or nx<0 or ny>=row or nx>=col:
                continue
                
            if maps[ny][nx] == 'X' or visited[ny][nx]:
                continue
                
            if maps[ny][nx] == 'E' and lever:
                visited[ny][nx] = visited[y][x] + 1
                break
            
            # lever 만나면 visited 초기화
            if not lever and (maps[ny][nx] == 'L'):
                prev = visited[y][x] + 1
                visited = [[0]*col for _ in range(row)]
                visited[ny][nx] = prev
                dq.clear()
                dq.append((ny, nx))
                lever = True
                break     
            
            visited[ny][nx] = visited[y][x] + 1
            dq.append((ny, nx))

    if visited[ey][ex] <= 1 or not lever:
        return -1
    else:
        return visited[ey][ex]-1


# print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
# print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
print(solution(["SOEOL","XXXXO","OOOOO","OXXXX","OOOOO"]))
print(solution(["SLEOX", "XXXXO", "OOOOO", "OXXXX", "OOOOO"]))
print(solution(["SELOX", "XXXXO", "OOOOO", "OXXXX", "OOOOO"]))
print(solution(["SLXOX", "EXXXO", "OOOOO", "OXXXX", "OOOOO"]))
print(solution(["SXXOX", "EXXXL", "OOXOO", "OXXXX", "OOOOO"]))
