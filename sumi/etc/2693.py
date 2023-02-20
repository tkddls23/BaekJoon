import sys

sys.stdin = open('index.txt')
input = sys.stdin.readline

MAX_SIZE = 1000000


def solution(arr):
    arr.sort(reverse=True)
    return arr[2]


if __name__ == "__main__":
    n   = int(input())
    for _ in range(n):
        arr = list(map(int, input().split()))
        res = solution(arr)
        print(res)
