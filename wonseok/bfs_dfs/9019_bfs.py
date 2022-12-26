# 9019 DSLR
from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    a, b = map(int,input().split())
    q = deque()
    q.append((a,""))
    visit = [False]*10000

    while q:
        num, commands = q.popleft()
        if num == b:
            print(commands)
            break
        # D
        target = (num*2)%10000
        if not visit[target]:
            q.append((target,commands+"D",))
            visit[target] = True
        # S
        target = (num-1)%10000
        if not visit[target]:
            q.append((target,commands+"S",))
            visit[target] = True
        # L
        target = (10*num+(num//1000))%10000
        if not visit[target]:
            q.append((target,commands+"L"))
            visit[target] = True
        # R
        target = (num//10+(num%10)*1000)%10000
        if not visit[target]:
            q.append((target,commands+"R"))
            visit[target] = True
