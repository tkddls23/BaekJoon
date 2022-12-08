# 1541 잃어버린 괄호
import re
from itertools import combinations, permutations

formula = input().split('-')
numbers = []

for i in formula:
    tmp = list(map(int,i.split('+')))
    numbers.append(sum(tmp))

result = numbers[0]

for i in range(1, len(numbers)):
    result -= numbers[i]

print(result)
