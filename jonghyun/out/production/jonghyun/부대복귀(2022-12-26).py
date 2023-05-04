from queue import Queue


def answerMapping(answerDict, sources):
    result = []
    print(answerDict)
    for source in sources :
        if source in answerDict :
            result.append(answerDict[source])
        else :
            result.append(-1)
    return result


def BFS(graph, check, sources, destination):
    Q = Queue()
    Q.put([destination, 0])
    check[destination] = True
    answerDic = {}
    if destination in sources :
        answerDic[destination] = 0
    while Q.empty() is not True :
        V = Q.get()
        for el in graph[V[0]] :
            if check[el] :
                continue
            check[el] = True
            Q.put([el, V[1] + 1])
            if el in sources :
                answerDic[el] = V[1] + 1
    return answerMapping(answerDic, sources)

def solution(n, roads, sources, destination):
    graph, check = initGraph(n, roads)
    answer = BFS(graph, check, sources, destination)
    print(answer)
    return answer


def initGraph(n, roads):
    check = [False for _ in range(n+2)]
    graph = [[] for _ in range(n+2)]
    for road in roads:
        graph[road[1]].append(road[0])
        graph[road[0]].append(road[1])
    return graph, check


solution(	5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5)