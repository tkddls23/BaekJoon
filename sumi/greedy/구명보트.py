from collections import deque


def solution(people, limit):
    answer = 0

    queue = deque()
    people.sort()
    for x in people:
        queue.append(x)

    while queue:
        tr = queue.pop()
        if not queue:
            answer += 1
            break;
        tl = queue.popleft()
        if tr + tl > limit:
            answer += 1
            queue.appendleft(tl)
        else:
            answer += 1
    return answer