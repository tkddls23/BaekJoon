import math
def solution(N):
    target_num = 52 - N
    min_val = 0
    max_val = 0
    if 40 <= target_num :
        max_val = 8
    else :
        max_val = target_num // 5

    if target_num <= 26 :
        min_val = 0
    else:
        min_val = math.ceil( (target_num - 26) / 2)


    if target_num == 39 :
        print(6, 7)

    min_val = min(min_val,max_val)

    print(min_val, max_val)



def init():
    N = int(input())
    solution(N)
init()
for i in range(53):
    print(52 - i, end= ": ")
    solution(i)


# import itertools
#
# def get_all_cases(n, k, max_val):
#     results = set()
#
#     for combo in itertools.combinations_with_replacement(range(max_val+1), k):
#         if sum(combo) == n:
#             results.add(tuple(sorted(combo)))
#
#     return sorted(list(results))
#
# result = get_all_cases(38, 13, 4)
# print(result)
