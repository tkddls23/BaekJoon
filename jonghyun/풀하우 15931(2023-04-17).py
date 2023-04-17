card_arr = [[i, j] for j in range(1, 14) for i in ["클로버", "하트", "스페이드", "다이아"]]


def solution(N):
    global card_arr
    target_num = 52 - N
    print(card_arr)



def init():
    N = int(input())
    solution(N)


solution(10)