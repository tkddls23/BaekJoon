# 오답... 이유?

from sys import stdin

a, b = map(int, stdin.readline().split())
n, m = map(int, stdin.readline().split())
arr = [[0]*a for _ in range(b)]
robots = {}

directions = ['E', 'S', 'W', 'N']

# 로봇 초기 위치
for i in range(n):
    x, y, dir = stdin.readline().split()
    robots[i+1] = (int(y)-1, int(x)-1, dir) # 1번 로봇 ~ M번 로봇 위치, 바라보는 방향

wall_crash = 0
robot_crash = []
# 로봇 이동 명령
for i in range(m):
    robot, order, repeat = stdin.readline().split()
    robot = int(robot)
    repeat = int(repeat)

    if(wall_crash or len(robot_crash)):
        continue

    ny, nx, nd = robots[robot]

    if(order == 'F'):
        if(nd == 'E'):            
            # 로봇과 충돌하는 경우
            for num, loc in robots.items():
                if(loc[0] == ny and nx < loc[1] <= nx+repeat):
                    robot_crash.append((robot, num, nd))
                    continue
                
            if(len(robot_crash)):
                continue
            
            # 벽과 충돌하는 경우
            if(nx + repeat > b-1):
                wall_crash = robot
                continue
            
            # 충돌 안했으면 위치 갱신
            robots[robot] = (ny, nx + repeat, nd)
        if(nd == 'W'):            
            for num, loc in robots.items():
                if(loc[0] == ny and nx-repeat <= loc[1] < nx):
                    robot_crash.append((robot, num, nd))
                    continue
                
            if(len(robot_crash)):
                continue
            
            if(nx - repeat < 0):
                wall_crash = robot
                continue
            
            robots[robot] = (ny, nx - repeat, nd)
        if(nd == 'S'):            
            for num, loc in robots.items():
                if(loc[1] == nx and ny-repeat <= loc[0] < ny):
                    robot_crash.append((robot, num, nd))
                    continue
                
            if(len(robot_crash)):
                continue
            
            if(ny - repeat < 0):
                wall_crash = robot
                continue
            
            robots[robot] = (ny-repeat, nx, nd)
        if(nd == 'N'):            
            for num, loc in robots.items():
                if(loc[1] == nx and ny < loc[0] <= ny+repeat):
                    robot_crash.append((robot, num, nd))
                    continue
                
            if(len(robot_crash)):
                continue
        
            if(ny + repeat > a-1):
                wall_crash = robot
                continue
            
            robots[robot] = (ny+repeat, nx, nd)
    
    if(order == 'L'):
        rotate = repeat % 4
        cur_idx = directions.index(nd)
        new_idx = (cur_idx - rotate) % 4

        robots[robot] = (ny, nx, directions[new_idx])

    if(order == 'R'):
        rotate = repeat % 4
        cur_idx = directions.index(nd)
        new_idx = (cur_idx + rotate) % 4

        robots[robot] = (ny, nx, directions[new_idx])

# print result
if(wall_crash):
    print(f'Robot {wall_crash} crashes into the wall')
elif(len(robot_crash)):
    if(robot_crash[0][2] == 'E' or robot_crash[0][2] == 'N'):
        robot_crash.sort(key=lambda x: x[1])
    else:
        robot_crash.sort(key=lambda x: -x[1])

    print(f'Robot {robot_crash[0][0]} crashes into robot {robot_crash[0][1]}')
else:
    print('OK')
