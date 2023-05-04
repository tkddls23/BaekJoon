def solution(N, M ,mi, ci) :

    # print(N, M, mi, ci)
    max_size = 10010
    dp = [[0 for _ in range(max_size)] for _ in range(105)]

    for index, value in enumerate(ci) :
        if index == 0 :
            for i in range(max_size) :
                if i >= value :
                    dp[index][i] = mi[index]
        else :
            for i in range(max_size) :
                if i - value >= 0 :
                    dp[index][i] = max(dp[index -1][i], dp[index - 1][i - value] + mi[index])
                else :
                    dp[index][i] = dp[index -1][i]


        # print(dp[index])
    for i in range(max_size) :
        if dp[N -1][i] >= M :
            print(i)
            break


def init() :
    N, M = map(int, input().split())
    mi = list(map(int, input().split()))
    ci = list(map(int, input().split()))
    solution(N, M, mi, ci)

# solution(5, 61, [30, 10, 20, 35, 40] ,[3, 0, 3, 5, 4])
init()