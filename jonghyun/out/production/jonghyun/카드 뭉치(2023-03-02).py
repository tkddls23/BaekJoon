def solution(cards1, cards2, goal):
    answer = ''

    index1 = 0
    index2 = 0

    for text in goal :
        if index1 < len(cards1) and text == cards1[index1] :
            index1 += 1
            continue
        if index2 < len(cards2) and text == cards2[index2] :
            index2 += 1
            continue
        return "No"


    return "Yes"


print(solution(	["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))