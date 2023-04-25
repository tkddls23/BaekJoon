from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

arr.sort()

psum = [0]*n
psum[0] = arr[0]

for i in range(1, n):
    psum[i] = psum[i-1]+arr[i]

print(sum(psum))
