from collections import deque

def solution(n, edge):
    #adj list
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
        
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    #bfs
    visited = [0 for i in range(n+1)]
    dq = deque([1])
    visited[1] = 1
    
    while dq:
        cur = dq.popleft()
        
        for g in graph[cur]:
            if(not visited[g]):
                visited[g] = visited[cur] + 1
                dq.append(g)
                
    #count most distant nodes
    ans = 0
    max_val = max(visited)
    for n in visited:
        if(n == max_val):
            ans += 1
            
    return ans
    
    