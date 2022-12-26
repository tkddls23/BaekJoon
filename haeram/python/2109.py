from sys import stdin

fee_arr = []
day_arr = []
dp = []

n = int(stdin.readline())

for i in range(n):
    p, d = map(int, stdin.readline().split())

    fee_arr.append(p)
    day_arr.append(d)

for it in day_arr:
    print(it)
    