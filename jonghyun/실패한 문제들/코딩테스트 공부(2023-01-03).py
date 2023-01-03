def initElement(width, length):
    return [[i + j for j in range(width)] for i in range(length)]


def fillDP(problem, DP, maxI, maxJ):
    for i in range(problem[0] + problem[2], maxI) :
        for j in range(problem[1] + problem[3], maxJ) :
            DP[i][j] = min(DP[i - problem[2]][j - problem[3]] + problem[4], DP[i][j])


def findMinTime(maxAlp, maxCop, maxI, maxJ, DP):
    minVal = 0xFFFFFF
    for i in range(maxAlp, maxI) :
        for j in range(maxCop, maxJ) :
            minVal = min(minVal, DP[i][j])
    return minVal


def solution(alp, cop, problems):
    maxI, maxJ = 150, 150
    DP = initElement(maxI, maxJ)
    for problem in problems :
        minusProblem(alp, problem, 0)
        minusProblem(cop, problem, 1)
    maxAlp, maxCop = max(problems, key = lambda x : x[0])[0], max(problems, key = lambda x : x[1])[1]
    for problem in problems :
        fillDP(problem, DP, maxI, maxJ)

    return findMinTime(maxAlp, maxCop, maxI, maxJ, DP)

def minusProblem(t, problem, i):
    if problem[i] - t < 0:
        problem[i] = 0
    else:
        problem[i] -= t