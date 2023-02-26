def solution(clothes):
    dict = {}
    for name, typed in clothes:
        if typed in dict:
            dict[typed] = dict[typed] + [name]
        else:
            dict[typed] = [name]

    answer = 1
    for key in dict:
        length = len(dict[key])
        answer *= length + 1
    return answer - 1