from sys import stdin

n, m = map(int, stdin.readline().split())
j = int(stdin.readline())

left = 1
right = m
cnt = 0

for _ in range(j):
    v = int(stdin.readline())

    if(v>=left and v<=right):
        continue

    if(v < left):
        gap = left-v

        cnt += gap
        left = v
        right = left+m-1

    if(v > right):
        gap = v-right

        cnt += gap
        right = v
        left = right-m + 1

print(cnt)
