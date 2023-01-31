from sys import stdin

n = int(stdin.readline())
stone = list(map(int, stdin.readline().split()))

count_max = 0
count_cur = 0
count_one = 0
count_two = 0
continue_flag = False

for s in range(len(stone)):
    if(stone[s] == 1):
        count_one+=1
    elif(stone[s] == 2):
        count_two+=1

    if(s==0):
        continue
        
    if(stone[s-1] == stone[s]):
        continue_flag = True
        count_cur += 1
    else:
        count_max = max(count_max, count_cur)
        count_cur = 0

if(count_max==0):
    print(1)
else:
    print(abs(count_one - count_two) + count_max)