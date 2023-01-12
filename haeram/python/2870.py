from sys import stdin

n = int(stdin.readline())
num_arr = []

for _ in range(n):
    str = stdin.readline()
    num_str = ''

    for s in str:
        if(s.isdigit()):
            num_str += s
            continue
        
        if(num_str):
            num_arr.append(int(num_str))
            num_str = ''

num_arr.sort()

for num in num_arr:
    print(num)
