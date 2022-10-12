# 9012 괄호
N = int(input())
PSDict = {}

def isVps(PS):
    s = 0
    if PS[-1] == "(" or PS[0] == ")":
        return "NO"
    while PS and s>=0:
        tmp = PS.pop()
        if tmp == ")":
            s += 1
        else:
            s -= 1
    if s == 0:
        return "YES"
    else:
        return "NO"
        

for i in range(N):
    PSDict[i] = list(input())

for i in range(len(PSDict)):
    print(isVps(PSDict[i]))
