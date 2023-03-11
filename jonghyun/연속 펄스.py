def solution(sequence):

    i1 = plus_start(sequence, 0)
    i2 = plus_start(sequence, 1)
    answer = max(i1, i2)
    return answer


def plus_start(sequence, idx):

    max_val = -0xFFFFFF
    sum = 0
    for i in sequence:

        if idx % 2 == 0 :
            sum += i
        else :
            sum += i * -1
        idx += 1

        max_val = max(max_val, sum)
        if sum < 0 :
            sum = 0

    return max_val

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))