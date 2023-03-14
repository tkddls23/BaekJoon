import sys
from collections import deque

sys.stdin = open('index.txt')
input = sys.stdin.readline

if __name__ == '__main__':

    n, m = map(int, input().split())
    arr = []
    for _ in range(m):
        arr.append(list(input().strip()))

    visited = set()
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    def bfs(start_node, color):
        que = deque()
        que.append(start_node)
        cnt = 0
        while que:
            cx, cy = que.pop()
            if (cx, cy) not in visited and 0 <= cx < m and 0 <= cy < n and arr[cx][cy] == color:
                visited.add((cx, cy))
                cnt += 1
                for dx, dy in d:
                    nx, ny = cx + dx, cy + dy
                    que.append((nx, ny))
        return cnt * cnt


    w_res = 0
    b_res = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] not in visited:
                cnt = bfs((i, j), arr[i][j])
                if arr[i][j] == 'W':
                    w_res += cnt
                else:
                    b_res += cnt

    print(w_res, b_res)
