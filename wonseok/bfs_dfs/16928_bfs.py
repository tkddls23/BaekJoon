# 16928 뱀과 사다리 게임
from sys import stdin
from collections import deque


def bfs(v):
    q = deque([v])
    visit[v] = True
    while q:
        now = q.popleft()
        # 1부터 6까지 bfs
        for move in range(1, 7):
            location = now + move
            if 0 < location <= 100 and not visit[location]:
                if location in ladder.keys():
                    location = ladder[location]

                if location in snake.keys():
                    location = snake[location]

                if not visit[location]:
                    q.append(location)
                    visit[location] = True
                    cnt[location] = cnt[now] + 1
    print(cnt[100])


# 사다리의 수 n 뱀의 수 m
n, m = map(int, stdin.readline().split())
ladder = {}
snake = {}
# 주사위 굴린 횟수, 방문 여부
cnt = [0] * 101
visit = [False] * 101

# 사다리 뱀 좌표 입력 배열보다 꺼내기 편해서 딕셔너리로 받음
for _ in range(n):
    i, j = map(int, stdin.readline().split())
    ladder[i] = j
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    snake[i] = j

bfs(1)