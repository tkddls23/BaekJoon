from collections import deque

a = 2
b = 5

queue = deque([[a, b]])

i = queue.popleft()

print(i)