from collections import deque

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def dfs(arr, start_node):
    N, M = len(arr), len(arr[0])
    visited = []
    stack = deque()

    stack.append((start_node[0], start_node[1], 1))
    while stack:
        x, y, cnt = stack.popleft()
        node = (x, y)

        if node not in visited:
            visited.append(node)
            for dx, dy in d:
                n_x, n_y = node[0] + dx, node[1] + dy
                if 0 <= n_x < N and 0 <= n_y < M and arr[n_x][n_y] == 1:

                    stack.append((n_x, n_y, cnt + 1))
                    if n_x == N - 1 and n_y == M - 1:
                        return cnt + 1
    return -1


def solution(maps):
    answer = 0
    res = dfs(maps, (0, 0))
    return res