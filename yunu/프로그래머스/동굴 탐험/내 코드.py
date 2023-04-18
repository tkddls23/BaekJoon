def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for v1, v2 in path:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    before = {} # { prev: next }
    after = {} # { next: prev }
    for v1, v2 in order:
        if v2 == 0:
            return False
        before[v1] = v2
        after[v2] = v1
    
    count = 0
    visited = [False for _ in range(n)]
    lock = set()
    unlock = set()
    queue = [0]
    while queue:
        v = queue.pop()
        visited[v] = True
        count += 1
        if count == n: return True
        for nv in graph[v]:
            if visited[nv]:
                continue
            if after.get(nv):
                if nv in unlock:
                    queue.append(nv)
                else:
                    lock.add(nv)
            elif before.get(nv):
                queue.append(nv)
                if before[nv] in lock:
                    queue.append(before[nv])
                else:
                    unlock.add(before[nv])
            else:
                queue.append(nv)
    
    return False

print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
print(solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]]))
print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))

'''
[dictionary로 방문 여부 체크]
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.13ms, 10.3MB)
테스트 4 〉	통과 (1.38ms, 10.5MB)
테스트 5 〉	통과 (0.65ms, 10.4MB)
테스트 6 〉	통과 (1.08ms, 10.4MB)
테스트 7 〉	통과 (0.09ms, 10.3MB)
테스트 8 〉	통과 (0.47ms, 10.2MB)
테스트 9 〉	통과 (1.00ms, 10.7MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.07ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.4MB)
테스트 13 〉	통과 (0.02ms, 10.4MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.08ms, 10.4MB)
테스트 16 〉	통과 (0.08ms, 10.2MB)
테스트 17 〉	통과 (0.92ms, 10.5MB)
테스트 18 〉	통과 (0.84ms, 10.6MB)
테스트 19 〉	통과 (0.86ms, 10.5MB)
테스트 20 〉	통과 (0.08ms, 10.3MB)
테스트 21 〉	통과 (0.07ms, 10.1MB)
테스트 22 〉	통과 (0.78ms, 10.6MB)
테스트 23 〉	통과 (0.03ms, 10.1MB)
테스트 24 〉	통과 (0.02ms, 10.3MB)
테스트 25 〉	통과 (0.14ms, 10.1MB)
테스트 26 〉	통과 (0.82ms, 10.6MB)
테스트 27 〉	통과 (0.09ms, 10.3MB)
테스트 28 〉	통과 (1.35ms, 10.5MB)
테스트 29 〉	통과 (0.02ms, 10.1MB)
테스트 30 〉	통과 (0.01ms, 10.2MB)
테스트 31 〉	통과 (0.01ms, 10.3MB)
테스트 32 〉	통과 (0.02ms, 10.2MB)
테스트 33 〉	통과 (0.43ms, 10.5MB)
테스트 34 〉	통과 (0.80ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (367.31ms, 90.3MB)
테스트 2 〉	통과 (368.29ms, 90.4MB)
테스트 3 〉	통과 (425.27ms, 91.1MB)
테스트 4 〉	통과 (379.51ms, 89.8MB)
테스트 5 〉	통과 (365.61ms, 90.5MB)
테스트 6 〉	통과 (377.91ms, 89.8MB)
테스트 7 〉	통과 (431.56ms, 91MB)
테스트 8 〉	통과 (391.13ms, 90.2MB)
테스트 9 〉	통과 (166.17ms, 93.3MB)
테스트 10 〉	통과 (235.28ms, 93.4MB)

[set으로 방문 여부 체크]
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.2MB)
테스트 4 〉	통과 (0.83ms, 10.6MB)
테스트 5 〉	통과 (0.38ms, 10.4MB)
테스트 6 〉	통과 (1.33ms, 10.6MB)
테스트 7 〉	통과 (0.08ms, 10.4MB)
테스트 8 〉	통과 (0.46ms, 10.3MB)
테스트 9 〉	통과 (0.55ms, 10.5MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.07ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.4MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
테스트 15 〉	통과 (0.08ms, 10.2MB)
테스트 16 〉	통과 (0.08ms, 10.4MB)
테스트 17 〉	통과 (0.86ms, 10.6MB)
테스트 18 〉	통과 (0.77ms, 10.5MB)
테스트 19 〉	통과 (0.78ms, 10.6MB)
테스트 20 〉	통과 (0.11ms, 10.3MB)
테스트 21 〉	통과 (0.07ms, 10.2MB)
테스트 22 〉	통과 (0.82ms, 10.5MB)
테스트 23 〉	통과 (0.02ms, 10.3MB)
테스트 24 〉	통과 (0.02ms, 10.4MB)
테스트 25 〉	통과 (0.08ms, 10.3MB)
테스트 26 〉	통과 (0.83ms, 10.5MB)
테스트 27 〉	통과 (0.08ms, 10.4MB)
테스트 28 〉	통과 (0.84ms, 10.6MB)
테스트 29 〉	통과 (0.02ms, 10.2MB)
테스트 30 〉	통과 (0.00ms, 10.3MB)
테스트 31 〉	통과 (0.03ms, 10.4MB)
테스트 32 〉	통과 (0.02ms, 10.3MB)
테스트 33 〉	통과 (0.77ms, 10.6MB)
테스트 34 〉	통과 (1.11ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (412.16ms, 90MB)
테스트 2 〉	통과 (411.86ms, 90.1MB)
테스트 3 〉	통과 (415.50ms, 91.5MB)
테스트 4 〉	통과 (365.05ms, 87.7MB)
테스트 5 〉	통과 (357.65ms, 88.5MB)
테스트 6 〉	통과 (369.60ms, 89.8MB)
테스트 7 〉	통과 (445.46ms, 91.2MB)
테스트 8 〉	통과 (383.04ms, 90.8MB)
테스트 9 〉	통과 (157.21ms, 90.1MB)
테스트 10 〉	통과 (223.65ms, 90MB)
'''