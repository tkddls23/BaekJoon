# 1012 유기농 배추

from sys import stdin

# 테스트 케이스 수 입력
t = int(stdin.readline())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [[x, y]]
    while queue:
        x, y = queue.pop()

        for i in range(4):  # 상하좌우로 탐색한다
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표가 matrix 범위 밖일때
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append([nx, ny])


for i in range(t):
    # 가로 세로 배추 개수
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    cnt = 0

    for j in range(K):
        # 배추 위치
        a, b = map(int, input().split())
        matrix[b][a] = 1

    for x in range(N):
        for y in range(M):
            # 배추가 있는곳 이라면
            if matrix[x][y] == 1:
                bfs(x, y)  # 인접한 배추 탐색
                matrix[x][y] = 0  # 탐색 완료
                cnt += 1
    print(cnt)
