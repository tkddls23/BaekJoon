from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
operator = list(map(int, stdin.readline().split())) # +, -, *, /

ans_max = -1e9
ans_min = 1e9
orders = [-1]*n

def calc(ops):
    ret = arr[0]

    for i in range(n):
        if(ops[i] == 0):
            ret += arr[i+1]
        elif(ops[i] == 1):
            ret -= arr[i+1]
        elif(ops[i] == 2):
            ret *= arr[i+1]
        elif(ops[i] == 3):
            ret = int(ret / arr[i+1])

    return ret


def dfs(depth):
    global ans_min, ans_max

    if(depth == n-1):
        cand = calc(orders)
        ans_max = max(cand, ans_max)
        ans_min = min(cand, ans_min)
        return
    
    for i in range(4):
        if(operator[i] == 0):
            continue
        
        orders[depth] = i
        operator[i] -= 1
        dfs(depth+1)

        orders[depth] = -1
        operator[i] += 1

dfs(0)

print(ans_max)
print(ans_min)      
