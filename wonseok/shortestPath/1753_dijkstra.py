# 1753 최단경로
from sys import stdin
import heapq

v, e = map(int,stdin.readline().split())
k = int(stdin.readline())
INF = int(1e9)

# 노드별로 연결된 노드 정보를 저장할 리스트 선언
graph = [[] for i in range(v + 1)]

# 최단 거리 테이블: 초기에는 모든 값을 무한으로 초기화
distance = [INF] * (v + 1)

# 간선 정보 입력받기
for _ in range(e):
    # 노드 A에서 노드 B로 가는 비용이 cost
    a, b, cost = map(int, stdin.readline().split())
    graph[a].append([b, cost])

def dijkstra(start):
    # 우선순위 큐 자료구조 생성
    queue = []
    # 시작 노드의 자기 자신까지의 거리는 0으로 설정, 우선순위 큐에 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    # 우선순위 큐가 비어있을 때까지 무한 반복
    while queue:
        # 최단 거리가 가장 짧은 노드 추출(거리, 노드 정보 순)
        dist, n_now = heapq.heappop(queue)

        # 이미 처리된 노드는 무시
        if distance[n_now] < dist:
            continue

        # 현재 처리 중인 노드와 인접한 노드 확인
        for i in graph[n_now]:
            c = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 가는 거리가 더 짧은 경우
            if c < distance[i[0]]:
                # 최단 거리 테이블 갱신
                distance[i[0]] = c
                # 우선순위 큐에 (거리, 노드 정보) 삽입
                heapq.heappush(queue, (c, i[0]))

# 다익스트라 알고리즘 구동
dijkstra(k)

for i in range(1, v + 1):
    # 노드를 방문할 수 없는 경우, '무한' 값 출력
    if distance[i] == INF:
        print("INF")
    # 노드를 방문할 수 있을 경우, 최단 거리 출력
    else:
        print(distance[i])
