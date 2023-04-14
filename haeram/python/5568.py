from sys import stdin
from itertools import permutations

n = int(stdin.readline())
k = int(stdin.readline())

numbers = [int(stdin.readline()) for _ in range(n)]

cands = permutations(numbers, k)
s = set()

for cand in cands:
    temp = ''
    for i in range(k):
        temp += str(cand[i])
    
    s.add(temp)

print(len(s))
