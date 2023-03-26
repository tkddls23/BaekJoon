from sys import stdin

p, m = map(int, stdin.readline().split())

rooms = [] # [0, []] 형태

for _ in range(p):
    l, n = stdin.readline().split()
    l = int(l)

    # 들어갈 방 있나 탐색
    entered = False
    for i in range(len(rooms)):
        if(len(rooms[i][1]) == m):
            continue
        
        if(abs(rooms[i][0] - l) <= 10):
            rooms[i][1].append((l, n))
            entered = True
            break

    # 들어간 방 없으면 방 만들기
    if(not entered):
        rooms.append([l, [(l, n)]])

print(rooms)

for room in rooms:
    room[1].sort(key=lambda x: x[1])

    # 방이 꽉찼으면 시작
    if(len(room[1]) == m):
        print('Started!')
    else:
        print('Waiting!')

    for player in room[1]:
        print(*player)
