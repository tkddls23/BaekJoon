check = [0 for _ in range(20_000)]
flag = False
def solution(graph):
    global check, flag

    for index, vertex in enumerate(graph) :
        if check[index] != 0 :
            continue
        dfs(index, graph, 1)


        if flag:
            break





def dfs(index, graph, value):
    global check, flag
    for x, vertex in enumerate(graph[index]):


        if flag:
            break


        opposite_value = get_opposite_value(value)
        if (check[index] != 0) and (check[index] != value):
            flag = True
            break
        check[index] = value
        dfs(vertex, graph, opposite_value)



def get_opposite_value(value):
    opposite_val = 2
    if value == 1:
        opposite_val = 2
    if value == 2:
        opposite_val = 1
    return opposite_val


def init() :
    global check, flag
    K = int(input())

    for i in range(K) :
        flag = False
        V, E = list(map(int, input().split()))

        graph = [[] for _ in range(20000)]
        for i in range(E):
            v1, v2 = list(map(int, input().split()))
            graph[v1].append(v2)
            graph[v2].append(v1)

        solution(graph)
        if flag:
            print("NO")
        else :
            print("YES")

init()