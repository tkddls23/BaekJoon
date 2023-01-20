def solution(brown, yellow):
    answer = []

    outer = (brown - 4) // 2
    inner = yellow
    res = 3
    res2 = 3

    for x in range(1, inner):
        w = outer - x
        if x * w == yellow:
            res = w + 2  # yellow, brown이 공유하고 있는 부분 + 2 => 전체 한변 길이
            res2 = x + 2
            break
    result = [res, res2]
    return sorted(result, reverse=True)