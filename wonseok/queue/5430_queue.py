# 5430 AC
from sys import stdin
from collections import deque
t = int(stdin.readline())

for _ in range(t):
    p = stdin.readline().rstrip()
    n = int(stdin.readline())
    arr = stdin.readline().rstrip().lstrip('[').rstrip(']')
    if arr:
        arr = list(map(int, arr.split(',')))
    queue = deque(arr)
    flag = 1
    stop = 0

    for i in p:
        if i == 'R' and len(queue):
            flag *= -1
        if i == 'D':
            if len(queue) == 0:
                print("error")
                stop = 1
                break
            try:
                if flag == -1:
                    queue.pop()
                else:
                    queue.popleft()
            except:
                print("error")
                stop = 1
                break

    if stop != 1:
        if flag == -1:
            queue.reverse()
        print('[', end="")
        if len(queue):
            for i in range(len(queue)-1):
                print(queue[i], end=',')
            print(f'{queue[-1]}]')
        else:
            print(']')