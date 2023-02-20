# 16236 아기 상어
# BFS는 BFS인데 같은 위치에 있는 먹이를 먹을때 조건을 생각해야해서 까다로웠다
from collections import deque
from sys import stdin


# 상어의 현재 위치에서 bfs
def bfs(a, b):
    visit = [[0] * n for _ in range(n)]  # 방문한 곳인지 체크
    queue = deque([[a,b]])
    candidate = []

    visit[a][b] = 1

    while queue:
        i, j = queue.popleft()

        for idx in range(4):
            ax, by = i + dx[idx], j + dy[idx]

            if 0 <= ax and ax < n and 0 <= by and by < n and visit[ax][by] == 0:
                # 상하 좌우 bfs 하는데 조건 설정
                # 물고기 먹을수 있는 경우
                if matrix[a][b] > matrix[ax][by] and matrix[ax][by] != 0:
                    visit[ax][by] = visit[i][j] + 1
                    candidate.append((visit[ax][by] - 1, ax, by))
                # 크기는 같아서 지나갈수있는 경우
                if matrix[a][b] == matrix[ax][by]:
                    visit[ax][by] = visit[i][j] + 1
                    queue.append([ax, by])
                # 비어있는 경우
                if matrix[ax][by] == 0:
                    visit[ax][by] = visit[i][j] + 1
                    queue.append([ax, by])

    # 6. 후보 리스트는 우선 순위가 있기 때문에 정렬을 사용할 수 있다. (가까운순, 위에있는순, 왼쪽에있는순)
    return sorted(candidate, key=lambda x: (x[0], x[1], x[2]))


n = int(stdin.readline())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
pos = []  # 상어 위치

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            pos.append(i)
            pos.append(j)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

totalTime = 0  # 물고기를 다 먹는데 걸린 시간
size = [2, 0]  # 상어의 사이즈, 먹은 먹이 물고기 수
a, b = pos  # 상어 위치

while True:
    matrix[a][b] = size[0]
    candidate = deque(bfs(a, b))

    if not candidate:
        break

    time, x, y = candidate.popleft()
    totalTime += time
    size[1] += 1

    # 자기 사이즈 만큼 먹었으면 사이즈 키우고 물고기 카운트 초기화
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    matrix[a][b] = 0
    a, b = x, y

print(totalTime)
