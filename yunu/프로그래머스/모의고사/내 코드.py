def solution(answers):
    retire1 = [1, 2, 3, 4, 5] # 5 * 2000
    retire2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8 * 1250
    retire3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10 * 1000
    
    retires = [retire1 * 2000, retire2 * 1250, retire3 * 1000]
    
    matchs = []
    maxMatch = 0
    for i, retire in enumerate(retires):
        count = 0
        for n1, n2 in zip(retire, answers):
            if n1 == n2:
                count += 1
        maxMatch = max(maxMatch, count)
        matchs.append(count)

    answer = []
    for i, match in enumerate(matchs):
        if match == maxMatch:
            answer.append(i + 1)
    
    return answer