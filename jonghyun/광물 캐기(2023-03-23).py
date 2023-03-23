from itertools import permutations
from itertools import combinations

def diamond_pick(five_mineral):
    ret = 0
    for i in five_mineral :
        if i == "diamond" :
            ret += 1
        if i == "iron" :
            ret += 1
        if i == "stone" :
            ret += 1
    return ret

def iron_pick(five_mineral):
    ret = 0
    for i in five_mineral:
        if i == "diamond":
            ret += 5
        if i == "iron":
            ret += 1
        if i == "stone":
            ret += 1
    return ret

def stone_pick(five_mineral):
    ret = 0
    for i in five_mineral:
        if i == "diamond":
            ret += 25
        if i == "iron":
            ret += 5
        if i == "stone":
            ret += 1
    return ret

def solution(picks, minerals):
    answer = 0xFFFFFF

    picks_sum = sum(picks)
    if len(minerals) > picks_sum * 5 :
        minerals = minerals[:picks_sum * 5]

    mineral_sum_arr = []

    temp = 1

    if len(minerals) % 5 == 0:
        temp = 0
    for i in range(len(minerals) // 5 + temp) :

        five_mineral = minerals[5 * i:(5 * (i + 1))]
        mineral_sum_arr.append([diamond_pick(five_mineral), iron_pick(five_mineral), stone_pick(five_mineral)])


    arr = []
    while len(mineral_sum_arr) > len(arr):
        if picks[0] > 0 :
            picks[0] -= 1
            arr.append(0)
            continue
        if picks[1] > 0 :
            picks[1] -= 1
            arr.append(1)
            continue
        if picks[2] > 0 :
            picks[2] -= 1
            arr.append(2)
            continue

    P = list(permutations(arr, len(arr)))

    for p in P:
        temp = 0
        len_p = len(p)
        for i in range(len_p) :
            temp += mineral_sum_arr[i][p[i]]
        answer = min(temp, answer)

    return answer


# print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
# print(solution(	[0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))

print(solution(	[5, 5, 5], [
    "diamond", "diamond", "diamond", "diamond", "diamond",
    "iron", "iron", "iron", "iron", "iron",
    "iron", "iron", "iron", "iron", "iron",
"iron", "iron", "iron", "iron", "iron",
]))