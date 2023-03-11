from sys import stdin

arr = []

#input
n = int(stdin.readline())
for _ in range(n):
    arrive, inspect = map(int, stdin.readline().split())
    arr.append((arrive, inspect))

#sort
arr = sorted(arr, key=lambda x: (x[0], x[1]))


cur = 0

for arrival, time in arr:
    if(arrival > cur):
        cur = arrival

    cur += time

print(cur)