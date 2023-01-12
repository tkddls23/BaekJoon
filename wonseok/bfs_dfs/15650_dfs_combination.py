# 15650 N과 M
from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())

arr = [i+1 for i in range(n)]


for value in list(combinations(arr,m)):
    for i in value:
        print(i, end=" ")
    print()