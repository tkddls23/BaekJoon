# JadenCase 문자열 만들기

def solution(s):
    arr = s.split(' ')
    result = []

    for i in arr:
        result.append(i.capitalize())
    return ' '.join(result)


print(solution(input()))
