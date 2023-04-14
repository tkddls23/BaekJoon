from queue import PriorityQueue
import heapq

problem_list = []
N = 0

def solution(problem_list, N) :
    problem_list.sort(key=lambda p: (p[0], -p[1]))
    hq = []
    for problem in problem_list :
        if problem[0] <= len(hq) :
            min_val = hq[0]
            if min_val < problem[1] :
                heapq.heappop(hq)
                heapq.heappush(hq, problem[1])
        else:
            heapq.heappush(hq, problem[1])


    print(sum(hq))

def init():
    global problem_list, N
    N = int(input())
    for i in range(N) :
        problem_list.append(list(map(int, input().split())))
    solution(problem_list, N)


init()
# solution([[1, 6], [1, 7], [3, 2], [3, 1], [2, 4], [2, 5], [6, 1]], 7)