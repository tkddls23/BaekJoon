from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    flag = True
    rev = False
    rev_total = 0

    cmd = stdin.readline().rstrip()
    n = int(stdin.readline())

    arr = stdin.readline().rstrip().strip('[').strip(']')
    if(len(arr)):
        arr = list(map(int, arr.split(',')))

    dq = deque(arr)

    for i in cmd:
        if(i == 'R' and len(dq)):
            rev = not rev
            rev_total += 1
            continue
        
        if(i == 'D'):
            if(len(dq) == 0):
                flag = False
                break
            
            dq.popleft() if not rev else dq.pop()

    if(rev_total%2 == 1):
        dq.reverse()

    if(flag):
        if(len(dq)==0):
            print([])
            continue

        print('[', end="")
        for it in range(len(dq)-1):
            print(dq[it], end=',')
        print(f'{dq[-1]}]')
    else:
        print('error')
