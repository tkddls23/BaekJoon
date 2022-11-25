# '무한'을 의미하는 값으로 10억을 활용
INF = int(1e9)

# 노드와 간선의 개수를 각각 입력
n, m = map(int, input().split())

# 시작 노드 번호를 입력
start = int(input())

# 노드별 연결된 노드 정보를 저장할 리스트 선언
graph = [[] for i in range(n + 1)]
# 방문 이력을 저장할 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블: 초기에는 모든 값을 무한으로 초기화
distance = [INF] * (n + 1)

# 간선 정보 입력받기
for _ in range(m):
    # 노드 A에서 노드 B로 가는 비용이 cost
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])


# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드 번호 반환
def getMinNode():
    min_v = INF
    # 최단 거리가 가장 짧은 노드 번호(=인덱스)
    idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_v and not visited[i]:
            min_v = distance[i]
            idx = i
    return idx


def dijkstra(start):
    # 시작 노드의 최단 거리 및 방문이력 초기화
    distance[start] = 0
    visited[start] = True
    # 시작 노드와 연결된 각각의 노드 간의 거리
    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n - 1):
        # 최단 거리가 가장 짧은 노드를 선택하고 방문처리
        n_now = getMinNode()
        visited[n_now] = True

        # 현재 노드를 거쳐 다른 노드까지의 거리 계산
        for j in graph[n_now]:
            c = distance[n_now] + j[1]
            # 최단 거리 테이블 갱신 가능여부 체크
            if c < distance[j[0]]:
                distance[j[0]] = c


# 다익스트라 알고리즘 구동
dijkstra(start)

for i in range(1, n + 1):
    # 노드를 방문할 수 없는 경우, '무한' 값 출력
    if distance[i] == INF:
        print("INF")
    # 노드를 방문할 수 있을 경우, 최단 거리 출력
    else:
        print("{}번 노드까지 최단 거리: {}".format(i, distance[i]))
