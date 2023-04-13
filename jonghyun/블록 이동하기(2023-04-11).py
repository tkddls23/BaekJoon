check_board = []

def init():
    global check_board
    check_board[0][0]['가로'] = 0
    pass


def solution(board):
    global check_board

    for i in range(len(board)):
        check_board.append([])
        for j in range(len(board[0])):
            check_board[i].append({
                "가로": 0xFFFFFF,  # 거리,
                "세로": 0xFFFFFF
            })

    init()
    print(check_board)

    rotate(first_dot, second_dot)
    move()

    answer = 0
    return answer

solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])