def solution(n, s):
    answer = []
    몫 = s//n
    나머지 = s%n
    for i in range(n) :
        answer.append(몫)
    for j in range(1, 나머지+1) :
        answer[-j] += 1

    if 0 in answer :
        return [-1]
    return answer


print(solution(2,9))
print(solution(4, 11))

print(solution(10, 10000))