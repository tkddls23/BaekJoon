def checkValue(today_split, privacyList):
    dateList = privacyList[0]
    if today_split[0] > dateList[0] :
        return privacyList[1] + 1
    elif today_split[0] == dateList[0] :
        if today_split[1] > dateList[1] :
            return privacyList[1] + 1
        elif today_split[1] == dateList[1] :
            if today_split[2] >= dateList[2] :
                return privacyList[1] + 1
    return None


def solution(today, terms, privacies):
    index = 0
    termCheck = []
    answer = []
    termSet = {}
    for term in terms :
        term_split = term.split()
        termCheck.append(term_split[0])
        termSet.setdefault(term_split[0], int(term_split[1]))
        index += 1

    index2 = 0
    for privacy in privacies :
        privacy_split = privacy.split()
        privacies[index2] = [privacy_split[0], privacy_split[1]]
        index2 += 1

    index = 0
    today_split = list(map(int, today.split(".")))
    for privacy in privacies :
        if privacy[1] in termCheck :
            date_split = list(map(int, privacy[0].split(".")))
            date_split[1] += termSet[privacy[1]]
            while date_split[1] >= 13 :
                date_split[1] -= 12
                date_split[0] += 1
            tmp = checkValue(today_split, [date_split, index])
            if tmp is not None :
                answer.append(tmp)
        index += 1

    return answer

assert solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]) == [1,3]
assert solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]) == [1,4,5]
assert solution("2022.05.19", ["A 6", "B 12", "C 3", "D 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]) == [1,3]
assert solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 D"]) == [1,3]