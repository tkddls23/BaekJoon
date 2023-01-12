from sys import stdin

n = int(stdin.readline())
arr = []

for _ in range(n):
    s, e = map(int, stdin.readline().split())

    arr.append((s, e))

arr = sorted(arr, key=lambda x:(x[0], x[1]))

start = -10**9
end = -10**9
ans = 0

for a in arr:
    if(end < a[1]):
        start = max(end, a[0])
        end = a[1]
        ans += end-start

print(ans)