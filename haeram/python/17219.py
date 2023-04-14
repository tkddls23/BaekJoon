from sys import stdin

n, m = map(int, stdin.readline().split())
accounts = {}

for _ in range(n):
    site, pw = stdin.readline().split()
    accounts[site] = pw

for _ in range(m):
    find = stdin.readline().rstrip()
    print(accounts[find])
    