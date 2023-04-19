import heapq

def find(parent, x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, y, x):
    px = find(parent, x)
    py = find(parent, y)

    if px < py:
        parent[py] = px
    else:
        parent[px] = py


def solution(n, costs):        
    ans = 0

    parents = [0]*n
    for i in range(n):
        parents[i] = i

    hq = []
    for cost in costs:
        [y, x, val] = cost
        heapq.heappush(hq, (val, y, x))

    while hq:
        val, y, x = heapq.heappop(hq)

        if find(parents, y) != find(parents, x):
            ans += val # update value
            union(parents, y, x)

    return ans


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) #4