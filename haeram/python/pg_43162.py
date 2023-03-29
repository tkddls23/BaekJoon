def dfs(visited, array, now, n):
    visited[now] = True
    for c in range(n):
        if(not visited[c] and now != c and array[now][c] == 1):
            dfs(visited, array, c, n)    

def solution(n, computers):
    ans = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if(not visited[i]):
            dfs(visited, computers, i, n)
            ans += 1
            
    return ans