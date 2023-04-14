from sys import stdin

n, x = map(int, stdin.readline().split())
visitors = list(map(int, stdin.readline().split()))

window  = sum(visitors[:x])
cur_max = window 
cnt     = 1

for i in range(1, n-x+1):
    window = window - visitors[i-1] + visitors[i-1+x]

    if window > cur_max:
        cur_max = window
        cnt = 1
    elif window == cur_max:
        cnt += 1
                
if(cur_max == 0):
    print('SAD')
else:
    print(cur_max)
    print(cnt)
    