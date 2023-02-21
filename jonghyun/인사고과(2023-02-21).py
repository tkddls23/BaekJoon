from collections import deque


def answerCal(scores, myScore):
    answer = 0
    wA = myScore[0]
    wB = myScore[1]
    for score in scores :
        A = score[0]
        B = score[1]
        if wA < A and wB < B :
            return -1
        if (wA + wB) < (A + B) :
            answer += 1
    return answer + 1

def solution(scores):
    answer = 0
    myScore = scores[0]
    wA = myScore[0]
    wB = myScore[1]

    liveArr = []

    scores.sort(key=lambda x: (-x[0], x[1]))

    DQ = deque(scores)
    scores_pop = DQ.popleft()
    liveArr.append(scores_pop)
    maxB = scores_pop[1]
    while DQ :
        scores_pop = DQ.popleft()
        if maxB > scores_pop[1]:
            pass
        else :
            maxB = scores_pop[1]
            liveArr.append(scores_pop)

    # print("liveArr "  , liveArr)
    # answerCal(liveArr, myScore)

    return answerCal(liveArr, myScore)

# print( solution([[2, 2], [3, 2], [1, 4], [3, 2], [2, 1]]) )
# print( solution([[3,3],[2,100],[1,10],[3,3],[3,3],[3,5],[2,2],[2,3],[2,5]])) # 2
print( solution([[3,3],[2,100],[1,10],[3,5],[2,5]])) # 2
# [3,100] , [2, 3], [1, 10]
# print( solution([[1,50], [49, 49], [50, 50]])) # 2
# print([[1,50],[48,48],[49,47],[49,49],[50,50]]) #2