from collections import deque

def diff(origin, cand):
    ret = 0
    for i in range(len(origin)):
        if(origin[i] != cand[i]):
            ret += 1

    return ret


def solution(begin, target, words):
    if(target not in words):
        return 0

    visited = []
    dq = deque()
    dq.append([begin, 0])
    visited.append(begin)

    #bfs
    while dq:
        cur = dq.popleft()

        if(cur[0] == target):
            return cur[1]
        
        for w in words:
            if(w not in visited and diff(cur[0], w) == 1):
                dq.append([w, cur[1]+1])
                visited.append(w)


# solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"])
# solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"])