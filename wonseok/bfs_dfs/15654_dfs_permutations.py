# 15654 N과 M (5)
from sys import stdin
from itertools import combinations
from itertools import permutations
n, m = map(int, stdin.readline().split())

numbers = list(map(int, stdin.readline().split()))
numbers.sort()

for value in list(permutations(numbers,m)):
    for i in value:
        print(i, end=" ")
    print()
