import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def is_range(x, y, n, m):
    if 0 <= x <= n - 1 and 0 <= y <= m - 1:
        return True
    else:
        return False


def main(n, m, arr):
    visit = set()

    def change_position(node, position):
        x = node[0] + dx[position]
        y = node[1] + dy[position]

        if x < 0:
            x = n - 1
        if x >= n:
            x = 0
        if y < 0:
            y = m - 1
        if y >= m:
            y = 0
        return (x, y)

    def bfs(start_node):
        queue = deque()
        queue.append(start_node)
        while queue:
            node = queue.popleft()
            if node not in visit and is_range(node[0], node[1], n, m) and arr[node[0]][node[1]] == 0:
                visit.add(node)
                for i in range(4):
                    t = change_position(node, i)
                    queue.append(t)
        return visit

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 and not (i, j) in visit:
                bfs((i, j))
                cnt += 1
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    print(main(n, m, arr))