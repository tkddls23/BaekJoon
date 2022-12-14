# 9375 패션왕 신해빈
from sys import stdin
from itertools import combinations

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    clothes = {}
    clothes_num =1
    for _ in range(n):
        cloth, kind = stdin.readline().split()

        try:
            clothes[kind].append(cloth)
        except:
            clothes[kind] = [cloth]
    # (각 옷의 종류수 +1)*(각 옷의 종류수 +1)*... -1
    for i in list(clothes.values()):
        clothes_num *= len(i)+1
    print(clothes_num -1)