import sys
sys.setrecursionlimit(10**6)

def DFS(graph, check, idx, light) :
    check[idx] = True
    for child in graph[idx] :
        if check[child] :
            continue
        val = DFS(graph, check, child, light)
        if val == 0 :
            light[idx] = True
    if light[idx] :
        return 1
    return 0

def graphProcessing(graph, idx, n):
    light = [False for _ in range(n + 100)]
    check = [False for _ in range(n + 100)]
    DFS(graph, check, idx, light)
    answer = 0
    for l in light :
        if l :
            answer += 1
    return answer



def solution(n, lighthouse):
    childSize = [0 for _ in range(n+100)]
    childSize[0] = -1
    graph = [[] for _ in range(n+100)]
    for edge in lighthouse :
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        childSize[edge[0]] += 1
        childSize[edge[1]] += 1

    idx = childSize.index(max(childSize))
    return graphProcessing(graph, idx, n)

print( solution(2, [[1,2]]) )