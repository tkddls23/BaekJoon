import sys, math
from collections import deque

input = sys.stdin.readline

MAX_SIZE = 1000000


def solution(n, k):
    queue = deque()
    visited = set()
    queue.append((n, 0))
    # queue는 popleft, append를 이용해 구현, 선입선출

    while queue:
        position, time = queue.popleft()

        visited.add(position)
        if position == k:
            return time
        for next in [position + 1, position - 1, position * 2]:
            if 0 <= next < MAX_SIZE and next not in visited:
                visited.add(next)
                if next == position * 2:
                    queue.appendleft((next, time + 1))
                else:
                    queue.append((next, time + 1))

    return -1


if __name__ == "__main__":
    n, k = map(int, input().split())

    res = solution(n, k)
    print(res)
