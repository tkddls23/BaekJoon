from itertools import permutations

def go(k, arr):
    pirro = k
    cnt = 0

    for m, spent in arr:
        if m > pirro:
            # 탐험 불가
            return cnt
        pirro -= spent
        cnt += 1
    return cnt


def solution(k, dungeons):
    answer = 0
    for arr in permutations(dungeons, len(dungeons)):
        answer = max(go(k, arr), answer)
    return answer