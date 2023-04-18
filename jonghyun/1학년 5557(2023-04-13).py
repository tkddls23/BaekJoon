

def solution(N, num_arr) :
    target_num = num_arr[-1]
    num_arr.pop()

    dp = [[0 for _ in range(21)] for _ in range(100)]
    for index, num in enumerate(num_arr) :
        if index == 0 :
            dp[index][num] = 1
            continue

        for i in range(21) :
            if (i + num) <= 20 :
                dp[index][i + num] += dp[index - 1][i]
            if (i - num) >= 0 :
                dp[index][i - num] += dp[index - 1][i]

    print(dp[N -2][target_num])

def init() :
    N = int(input())
    problem_list = list(map(int, input().split()))
    solution(N, problem_list)

init()
# solution(11, [8, 3, 2, 4, 8, 7, 2, 4, 0, 8, 8])