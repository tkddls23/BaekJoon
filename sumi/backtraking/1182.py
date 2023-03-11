import sys
from itertools import combinations

sys.stdin = open('index.txt')
input = sys.stdin.readline

cnt = 0


def main(arr, s):
    cnt = 0
    for i in range(1, len(arr) + 1):
        for com in combinations(arr, i):
            res = sum(com)
            if res == s:
                cnt += 1
    return cnt


if __name__ == "__main__":
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    print(main(arr, s))
