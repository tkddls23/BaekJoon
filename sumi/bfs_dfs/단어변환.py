from collections import deque


def check_convert(w1, w2):
    a1 = list(w1)
    a2 = list(w2)
    cnt = 0
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            cnt += 1

    if cnt > 1:  return False
    return True


def solution(begin, target, words):
    answer = 0
    if not target in words:
        return 0
    max_length = len(words)

    def bfs(start):
        queue = deque()
        queue.append((start, 0))

        while queue:
            current, level = queue.popleft()
            # print(current, level)
            if current == target:
                return level
            if level == max_length + 1:
                return 0

            for x in words:
                if current != x and check_convert(current, x):
                    queue.append((x, level + 1))

    return bfs(begin)