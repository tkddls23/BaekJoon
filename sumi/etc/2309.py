import sys
from itertools import combinations

sys.stdin = open('index.txt')
input = sys.stdin.readline

def solution(arr):

    for combi in combinations(arr,7):
        if sum(combi) == 100:
            return sorted(combi)


if __name__ == "__main__":
    arr = []
    for _ in range(9):
        n = int(input())

        arr.append(n)
    res = solution(arr)
    for x in res:
        print(x)
    # print(res)
