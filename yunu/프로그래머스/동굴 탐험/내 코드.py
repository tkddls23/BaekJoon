from collections import deque

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for v1, v2 in path:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    before = {} # { prev: next }
    after = {} # { next: prev }
    for v1, v2 in order:
        before[v1] = v2
        after[v2] = v1
      
    count = 0
    visited = [False for _ in range(n)]
    lock = {} # { prev: next }
    unlock = {} # { next: prev }
    queue = deque([0])
    while queue:
        v = queue.popleft()
        visited[v] = True
        count += 1
        if count == n: return True
        for nv in graph[v]:
            if visited[nv]:
                continue
            if after.get(nv):
                if unlock.get(nv):
                    queue.append(nv)
                else:
                    lock[after[nv]] = nv
                continue
            if before.get(nv):
                queue.append(nv)
                if lock.get(nv):
                    queue.append(lock[nv])
                else:
                    unlock[before[nv]] = nv
                continue
            queue.append(nv)
    
    return False

print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
print(solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]]))
print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))