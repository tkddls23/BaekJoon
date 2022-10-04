# 9012 괄호
N = int(input())

def isVps(PS):
    for i in range(len(PS)):
        if PS[0] == ")" or PS[-1] == "(":
            print("NO")
        

for i in range(N):
    PS = list(input())
    isVps(PS)