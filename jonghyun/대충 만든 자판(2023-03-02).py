def solution(keymap, targets):
    dic = {}
    answer = []
    for i in range(65, 91):
        dic[chr(i)] = 10000

    for key in keymap:
        for i in range(len(key)):
            dic[key[i]] = min(dic[key[i]], i + 1)

    for target in targets :
        temp = 0
        flag = False
        for t in target :
            val = dic[t]
            if val == 10000 :
                flag = True
                answer.append(-1)
                break
            temp += val
        if flag is False :
            answer.append(temp)

    return answer

print(solution(	["ABACD", "BCEFD"], ["ABCD", "AABB"]))