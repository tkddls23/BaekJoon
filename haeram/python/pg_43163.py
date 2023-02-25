from collections import deque

def diff(origin, cand):
    ret = 0
    for i in range(len(origin)):
        if(origin[i] != cand[i]):
            ret += 1
            
    return ret


cnt = 0
def bfs(dq, visited, target):
    global cnt
    cur = ''

    while dq:
        cur = dq.popleft()
        visited.append(cur)

        if(cur == target):
            cnt += 1
            return
    
    cnt += 1
    return cur
    
    
def solution(begin, target, words):
    if(target not in words):
        return 0
    
    visited = []
    dq = deque()
    
    for i in range(len(words)):
        if(len(visited) == len(words)):
            return cnt
        
        for j in range(len(words)):
            if(words[j] not in visited and diff(begin, words[j]) == 1):
              dq.append(words[j])
        
        if(dq):
            new_begin = bfs(dq, visited, target)
            begin = new_begin
            
    return cnt
    

solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"])