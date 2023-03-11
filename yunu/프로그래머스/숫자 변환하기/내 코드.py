from collections import deque

def solution(x, y, n):
    cache = [-1 for _ in range(y + 1)]
    cache[x] = 0
    
    queue = deque([x])
    while queue:
        num1 = queue.popleft()
        if num1 == y: return cache[y]
        for num2 in [num1 + n, num1 * 2, num1 * 3]:
            if num2 > y: continue
            if cache[num2] != -1: continue
            cache[num2] = cache[num1] + 1
            queue.append(num2)
    
    return -1
    