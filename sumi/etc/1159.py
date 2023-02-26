import sys

sys.stdin = open('index.txt')
input = sys.stdin.readline

# https://www.acmicpc.net/problem/1159
if __name__ == "__main__":
    n = int(input())
    dict = {}

    for _ in range(n):
        t = input().strip()[0]
        if not t in dict:
            dict[t] = 0
        dict[t] += 1

    res = []
    for key in dict:
        if dict[key] >= 5:
            res.append(key)
    if len(res) ==0:
        print('PREDAJA')
    else:
        res.sort()
        print(''.join(res))