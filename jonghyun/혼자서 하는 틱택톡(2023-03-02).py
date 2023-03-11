global bingo_case
bingo_case = [[1,2,3], [4,5,6],[7,8,9],[1,4,7],[2,5,8], [3,6,9], [1,5,9], [3,5,7]]


def is_bingo(board, char):
    bingo = False
    index = 0
    temp_arr = []
    for arr in board:
        for i in arr:
            index += 1
            if i == char :
                temp_arr.append(index)

    for case in bingo_case :
        temp = 0
        for c in case :
            if c in temp_arr :
                temp += 1
            else:
                break
        if temp == 3 :
            bingo = True
    return bingo



def isYBingo(board):
    pass


def solution(board):
    O = 0
    X = 0
    dot = 0

    O, X = check_number(O, X, board, dot)
    if O < X or O > X + 1:
        return 0

    x_bingo = is_bingo(board,'X')
    o_bingo = is_bingo(board, 'O')

    if O == X and o_bingo == 1 :
        return 0
    if O == X + 1 and x_bingo == 1 :
        return 0

    if x_bingo == True and o_bingo == True :
        return 0
    return 1


def check_number(O, X, board, dot):
    for arr in board:
        for i in arr:
            if i == 'O':
                O += 1
            elif i == 'X':
                X += 1
            else:
                dot += 1
    return O, X

# print(solution(	["OOX", "OXX", "XOO"]))
# print(solution(	["..X", ".O.", "..."]))
# print(solution(	["..X", ".O.", "..."]))
# print(solution(	["XOX", "O.O", "XOX"]))
# print(solution(	["XOX", "OOO", "XOX"]))
# print(solution( ["OOO", "XX.", "X.."]))
print(solution(["OOX", "OXO", "XOO"]))
# print(solution(["OXO", "XOX", "OXO"]))
# print(solution(["OOX", "XXO", "OOX"]))
# print(solution(["XXX", ".OO", "O.."]))
# print(solution(["OX.", ".O.", ".XO"]))
# print(solution(["...", "...", ".O."]))
# print(solution(["X.X", "X.O", "O.O"]))
# print(solution(["XO.", "OXO", "XOX"]))
# print(solution(["OOO", "XOX", "XXO"]))
# print(solution(["OOO", "XOX", "X.X"]))
# print(solution(["XXX", "OO.", "OO."]))
# print(solution([".X.", "...", "..."]))
# print(solution([".X.", "X..", ".O."]))
# print(solution(["XOX", "OXO", "XOX"]))
# print(solution(["XXX", "XOO", "OOO"]))
# print(solution(["OOX", "OXO", "XOO"]))
# print(solution(["OOX", "OXO", "XOX"]))
# print(solution([".OX", "OXO", "XO."]))
# print(solution(["OOO", "XX.", "X.."]))