import sys
from collections import deque

sys.stdin = open('index.txt')
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# silver 1
# 최단 경로 bfs 문제
def is_range(x, y, n, m):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


def main(n, m, arr):
    def bfs(start_node):
        queue = deque()
        queue.append(start_node)
        while queue:
            node = queue.popleft()
            for i in range(4):
                nx = node[0] + dx[i]
                ny = node[1] + dy[i]
                if is_range(nx, ny, n, m) and arr[nx][ny] == 1:
                    queue.append((nx, ny))
                    arr[nx][ny] = arr[node[0]][node[1]] + 1
        return arr[n - 1][m - 1]

    return bfs((0, 0))


if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, list(input().strip()))))

    res = main(n, m, arr)
    print(res)
