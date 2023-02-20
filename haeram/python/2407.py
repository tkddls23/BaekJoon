from sys import stdin
from math import comb

n, m = map(int, stdin.readline().split())

print(comb(n, m))

