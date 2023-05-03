from sys import stdin

n = stdin.readline().rstrip()
length = len(n)

cand = []

def dfs(arr, depth):
    if depth == length:
        if arr[-1] == n and arr not in cand:
            cand.append(arr[:])
        return
    
    for i in range(10):
        cur = arr[-1]
        if (cur + str(i)) in n:
            arr.append(cur+str(i))
            dfs(arr, depth+1)
            arr.pop()
        if (str(i) + cur) in n:
            arr.append(str(i)+cur)
            dfs(arr, depth+1)
            arr.pop()
        
    
    return


for i in range(10):
    if str(i) in n:
        dfs([str(i)], 1)

print(len(cand))

