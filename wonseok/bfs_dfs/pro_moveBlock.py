from collections import deque


def solution(board):
    N = len(board)
    visited = set()
    queue = deque([((0, 0), (0, 1), 0)])
    visited.add(((0, 0), (0, 1)))
    while queue:
        first, second, result = queue.popleft()
        if first == (N - 1, N - 1) or second == (N - 1, N - 1):
            return result
        for pos in bfs(first, second, board):
            if pos not in visited:
                queue.append((pos[0], pos[1], result + 1))
                visited.add(pos)


def bfs(first, second, board):
    pos = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nextFirst = (first[0] + dx[i], first[1] + dy[i])
        nextSecond = (second[0] + dx[i], second[1] + dy[i])
        if isValid(nextFirst[0], nextFirst[1], board) and isValid(nextSecond[0], nextSecond[1], board):
            pos.append((nextFirst, nextSecond))
    if first[0] == second[0]:
        for i in [-1, 1]:
            if isValid(first[0] + i, first[1], board) and isValid(second[0] + i, second[1], board):
                pos.append((first, (first[0] + i, first[1])))
                pos.append((second, (second[0] + i, second[1])))
    elif first[1] == second[1]:
        for i in [-1, 1]:
            if isValid(first[0], first[1] + i, board) and isValid(second[0], second[1] + i, board):
                pos.append(((first[0], first[1] + i), first))
                pos.append(((second[0], second[1] + i), second))
    return pos


def isValid(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board) and board[x][y] == 0
