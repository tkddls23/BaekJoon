from sys import stdin
import math

n = int(stdin.readline())

for i in range(n):
    for _ in range(n-i-1):
        print(' ', end='')
    
    for _ in range((i+1)*2 - 1):
        print('*', end='')

    print()

for i in range(3):
    for _ in range(math.ceil(n/2)):
        print(' ', end='')
    
    for _ in range(math.ceil(n/2)+1):
        print('*', end='')
    
    print()