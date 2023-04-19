def solution(N, ni, M, mi)  :
    # print(N, ni, M, mi)

    stop = 30 * 505
    dp = [[0 for _ in range(stop)] for _ in range(31)]

    for index, value in enumerate(ni):
        if index == 0 :
            dp[index][value] = 1
        else :
            dp[index][value] = 1
            for i in range(stop) :
                dp[index][i] = max(dp[index - 1][i], dp[index][i])
                if dp[index - 1][i] == 1 :
                    dp[index][abs((i * -1) + value)] = 1
                    if i + value <= 15000 :
                        dp[index][i + value] = 1

    # for i, v in enumerate(dp[N-1]) :
    #     print("[", i, ",", v, "]", end= " , ")

    for i in mi :
        if i > 15000 :
            print("N", end=" ")
            continue
        if dp[N -1][i] == 1 or dp[N -1][i] == 1 :
            print("Y", end=" ")
        else :
            print("N", end=" ")

def init():
    N = int(input())
    ni = list(map(int, input().split()))
    M = int(input())
    mi = list(map(int, input().split()))
    solution(N, ni, M, mi)

# solution(2, [1, 4], 2, [3, 2])
# solution(4, [2, 3, 3, 3], 3, [1, 4, 10])
init()
