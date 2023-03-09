def solution(n, m, section):
    arr = [0 for _ in range(n+1)]

    answer = 0
    for i in section :
        if arr[i] == 1 :
            continue
        answer += 1
        for j in range(i, i + m) :
            if j >= n+1 :
                continue
            arr[j] = 1

    return answer

# print(solution(8, 4, [2, 3, 6]))
# print(solution(	5, 4, [1, 3]))
# print(solution(4, 1, [1, 2, 3, 4]))
print(solution(5, 5, [1,3,5]))