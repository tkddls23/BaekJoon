from itertools import combinations, permutations, product

real_board = []
score = 0
direction = [[1,0], [-1,0], [0,1], [0,-1]]


def shot(board, target, damage):
    for key, value in enumerate(board[target]) :
        global score
        if value <= 0 :
            continue
        elif value >= 10 :
            board[target][key] = 0
            score += value
            return
        else :
            board[target][key] -= damage
            if board[target][key] <= 0 :
                global real_board, direction
                score += real_board[target][key]
                for di in direction :
                    x = target + di[0]
                    y = key + di[1]
                    if x < 0 or y < 0 or x >= len(board) or y >= len(board) :
                        continue
                    if board[x][y] > 0 :
                        continue
                    board[x][y] = real_board[target][key] // 4
                    real_board[x][y] = real_board[target][key] // 4
            return


def solution(N, K, board, shot_array) :

    board_sizes = [i for i in range(len(board))]
    answer = -0xFFFFFF
    for i in product(board_sizes, repeat=len(shot_array)) :
        global real_board
        real_board = [item[:] for item in board]
        board_copy = [item[:] for item in board]

        global score
        score = 0

        for key, j in enumerate(i) :
            shot(board_copy, j, damage= shot_array[key])

        answer = max(answer, score)

    return answer



def init():
    N = int(input())
    K = int(input())
    board = []
    for i in range(N):
        li = list(map(int, input().split()))
        board.append(li)
    shot_array = list(map(int, input().split()))
    print(solution(N, K, board, shot_array))


init()
# print(solution(5,3 ,[[0, 0, 0, 0, 0], [10, 0, 4, 0, 0], [0, 0, 7, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, 0, 0]] ,[1, 5, 1]))
# print(solution(5,5 ,[[0, 0, 7, 0, 0], [0, 0, 5, 20, 20], [0, 6, 7, 0, 0], [0, 1, 0, 0, 0], [0, 0, 2, 0, 0]] ,[2, 3, 1, 1, 1]))