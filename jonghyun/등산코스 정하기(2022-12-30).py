from queue import PriorityQueue
import heapq

def solution(n, paths, gates, summits):
    h = []
    summits.sort()
    summitsCheck = 0
    summits = set(summits)
    gates = set(gates)
    graph = [[] for _ in range(len(paths) + 10)]
    visited = [0 for _ in range(len(paths) + 10)]
    for path in paths:
        graph[path[0]].append([path[1], path[2]])
        graph[path[1]].append([path[0], path[2]])

    for gate in gates:
        for i in graph[gate]:
            if i[0] not in gates :
                visited[gate] = 1
                heapq.heappush(h, [i[1], i[0]])
                # visited[i[0]] = 1


    answerArr = []
    answerVal = 0
    temp = -1
    while len(h) != 0:
        element = heapq.heappop(h)
        # visited[element[1]] = 1

        if temp != -1:
            if temp < element[0]:
                return min(answerArr)

        if summitsCheck == len(summits) :
            return min(answerArr)

        answerVal = max(answerVal, element[0])

        if element[1] in summits:
            answerArr.append([element[1], answerVal])
            temp = answerVal
            summitsCheck += 1
            continue

        for i in graph[element[1]]:
            if visited[i[0]] != 0:
                continue
            visited[element[1]] = 1
            heapq.heappush(h, [i[1], i[0]])
    return min(answerArr)



# arr = [[i, i+1, i] for i in range(1, 100_000)]
# arr.extend([i, i+1, i] for i in range(100_000, 200_000))
# print( solution(	7, arr, [i for i in range(1, 25_000)], [i for i in range(49_999, 50_000)]) )
print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
# print( solution(	7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [2], [3, 4]) )