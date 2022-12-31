from queue import PriorityQueue


def solution(n, paths, gates, summits):
    PQ = PriorityQueue()
    graph = [[] for _ in range(len(paths) + 10)]
    visited = [0 for _ in range(len(paths) + 10)]
    for path in paths:
        graph[path[0]].append([path[1], path[2]])
        graph[path[1]].append([path[0], path[2]])

    for gate in gates:
        for i in graph[gate]:
            PQ.put([i[1], i[0]])

    answerArr = []
    answerVal = 0
    temp = -1
    while PQ.empty() is not True:
        element = PQ.get()
        visited[element[1]] = 1

        if temp != -1 :
            if temp < element[0] :
                return min(answerArr)

        answerVal = max(answerVal, element[0])

        if element[1] in summits:
            answerArr.append([element[1], answerVal])
            temp = answerVal
            continue

        for i in graph[element[1]]:
            if visited[i[0]] != 0 :
                continue
            PQ.put([i[1], i[0]])
    return min(answerArr)

print( solution(	7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [2], [3, 4]) )