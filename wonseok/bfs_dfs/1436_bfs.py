# 1436 영화감독 숌
from sys import stdin 

N = int(stdin.readline())
first = 666

while N != 0:
    if '666' in str(first):
        N -= 1 
        if N == 0:
            break       
    first +=1

print(first)