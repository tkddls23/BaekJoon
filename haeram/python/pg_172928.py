def solution(park, routes):
    # get start point
    sy = 0
    sx = 0
    
    row_len = len(park)
    col_len = len(park[0])
    
    for i in range(row_len):
        for j in range(col_len):
            if(park[i][j] == 'S'):
                sy = i
                sx = j
                break
                
    # move robot
    for route in routes:        
        d, m = route.split()
        m = int(m)
        is_val = True
        
        if(d == 'E'):
            for i in range(sx, sx+m+1):
                if(i >= col_len or park[sy][i] == 'X'):
                    is_val = False
                    break

            if(is_val):
                sx = sx+m
        elif(d == 'S'):
            for i in range(sy, sy+m+1):
                if(i >= row_len or park[i][sx] == 'X'):
                    is_val = False
                    break
                    
            if(is_val):
                sy = sy+m
        elif(d == 'W'):
            for i in range(sx-1, sx-m-1, -1):
                if(i < 0 or park[sy][i] == 'X'):
                    is_val = False
                    break
                    
            if(is_val):
                sx = sx-m
        elif(d == 'N'):
            for i in range(sy-1, sy-m-1, -1):
                if(i < 0 or park[i][sx] == 'X'):
                    is_val = False
                    break
                    
            if(is_val):
                sy = sy-m
                
    return [sy, sx]
