# 1865 웜홀
from sys import stdin

INF = int(1e9)


def bellman_ford(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    for i in range(n):
        for s, e, t in edges:  # 출발, 도착, 비용
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n - 1:  # 모든 노드를 확인한 경우
                    return True
    return False


tc = int(stdin.readline())

for _ in range(tc):
    n, m, w = map(int, stdin.readline().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, stdin.readline().split())
        edges.append((s, e, t))
        edges.append((e, s, t))  # 무방향
    for _ in range(w):
        s, e, t = map(int, stdin.readline().split())
        edges.append((s, e, -t))

    if bellman_ford(1):
        print("YES")
    else:
        print("NO")
