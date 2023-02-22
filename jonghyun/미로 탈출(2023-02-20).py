from collections import deque


def findStartAndLever(maps):
    start = [0, 0]
    lever = [0, 0]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                start = [i, j]
            if maps[i][j] == "L":
                lever = [i, j]
    return start


def BFS(maps, start, end_char):
    check = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    lengthList = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    DQ = deque()
    DQ.append(start)

    while DQ:
        popleft = DQ.popleft()
        for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x = popleft[0] + i[0]
            y = popleft[1] + i[1]
            if x < 0 or y < 0 or x >= len(maps) or y >= len(maps[0]) or maps[x][y] == "X":
                continue
            if check[x][y] == 1:
                continue
            if maps[x][y] == end_char:
                return [lengthList[popleft[0]][popleft[1]] + 1, [x, y]]
            lengthList[x][y] = lengthList[popleft[0]][popleft[1]] + 1
            check[x][y] = 1
            DQ.append([x, y])
    print(-1)
    return [-111111, 1]


def solution(maps):
    start = findStartAndLever(maps)
    lever_length, lever = BFS(maps, start, "L")
    if lever_length == -111111 :
        return -1
    end_length, end = BFS(maps, lever, "E")
    if end_length == -111111 :
        return -1
    answer = lever_length + end_length
    print(answer)
    return answer


solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"])
solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"])
