# 13549 숨바꼭질 3
from collections import deque
from sys import stdin

MAX = 10 ** 5


def bfs(n, k):
    distance = [-1] * (MAX + 1)
    distance[n] = 0
    visited = [False] * (MAX + 1)

    queue = deque([n])

    while queue:
        node = queue.popleft()
        if node == k:
            return distance[node]
        for neighbor in (node - 1, node + 1, node * 2):
            if 0 <= neighbor <= MAX and not visited[neighbor]:
                visited[neighbor] = True
                if neighbor == node * 2:
                    distance[neighbor] = distance[node]
                    queue.appendleft(neighbor)
                else:
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)


n, k = map(int, stdin.readline().split())
print(bfs(n, k))
