from collections import defaultdict

def solution(board):
    
    def fillBlack():
        filled = [False for _ in board[0]]
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == -1:
                    continue
                if board[y][x] != 0:
                    filled[x] = True
                if not filled[x] and board[y][x] == 0:
                    board[y][x] = -1
    
    def removeRect():
        count = 0
        rect1 = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]]
        rect2 = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
        
        for y in range(len(board) - 1):
            for x in range(len(board[y]) - 2):
                type = defaultdict(int)
                for dy, dx in rect1:
                    type[board[y + dy][x + dx]] += 1
                if len(type) == 2 and type[-1] == 2 and type[0] == 0:
                    count += 1
                    for dy, dx in rect1:
                        board[y + dy][x + dx] = 0
        
        for y in range(len(board) - 2):
            for x in range(len(board[y]) - 1):
                type = defaultdict(int)
                for dy, dx in rect2:
                    type[board[y + dy][x + dx]] += 1
                if len(type) == 2 and type[-1] == 2 and type[0] == 0:
                    count += 1
                    for dy, dx in rect2:
                        board[y + dy][x + dx] = 0
        
        return count
    
    answer = 0
    fillBlack()
    count = removeRect()
    answer += count
    while count > 0:
        fillBlack()
        count = removeRect()
        answer += count
        
    return answer