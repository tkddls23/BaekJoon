def solution(survey, choices):
    total = { type: 0 for type in 'RTCFJMAN' }
    
    for type, point in zip(survey, choices):
        if point < 4:
            total[type[0]] += 4 - point
        else:
            total[type[1]] += point - 4
    
    answer = ''
    for type1, type2 in ['RT', 'CF', 'JM', 'AN']:
        if total[type2] > total[type1]:
            answer += type2
            continue
        answer += type1
    
    return answer
