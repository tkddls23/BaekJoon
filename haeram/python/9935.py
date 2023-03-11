from sys import stdin

str = stdin.readline().rstrip()
blow = stdin.readline().rstrip()

# ret = ""
# for s in str:
#     ret += s
#     if(len(ret)>=len(blow) and ret[-len(blow):] == blow):
#         ret = ret[0:len(ret)-len(blow)]
    
# if(len(ret) == 0):
#     print("FRULA")
# else:
#     print(ret)


stk = []

for s in str:
    stk.append(s)

    if(len(stk)>=len(blow) and ''.join(stk[-len(blow):]) == blow):
        for _ in range(len(blow)):
            stk.pop()

if(len(stk) == 0):
    print('FRULA')
else:
    print(''.join(stk))

