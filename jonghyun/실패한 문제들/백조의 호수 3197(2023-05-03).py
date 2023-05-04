check = []
board = []


def solution():
    pass


def init():
    global check, board
    R, C = list(map(int, input().split()))
    check = [[-1 for _ in range(C)] for _ in range(R)]
    for i in range(R) :
        board.append(list(input()))
    print(board)
    solution()

init()