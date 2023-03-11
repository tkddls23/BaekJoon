# 최댓값과 최솟값

def solution(s):
    arr = list(map(int, s.split()))
    result = [min(arr), max(arr)]
    answer = " ".join(map(str, result))

    return answer


print(solution(input()))
