# 18111 마인크래프트
from sys import maxsize, stdin 

vertical,width,block = map(int,stdin.readline().split())
result = 1000000000000000
floor = 0

craft = [list(map(int, stdin.readline().split())) for _ in range(vertical)]

for i in range(257):
    plus = 0
    minus = 0
    for x in range(vertical):
        for y in range(width):
            if craft[x][y] >i:
                minus += craft[x][y] - i
            else:
                plus += i - craft[x][y]
    
    
    if plus <= minus + block:
        if minus *2 + plus <= result:
            result = minus *2 + plus
            floor = i

print(result, floor)