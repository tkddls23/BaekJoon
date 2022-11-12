from sys import stdin 

N, M, V = map(int,stdin.readline().split())


matrix = [[0] * (N+1) for i in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    a, b = map(int,stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(V):
    visited[V] = 1
    print(V, end=' ')

    for i in range(1, N+1):
        if(visited[i]==0 and matrix[V][i] == 1):
            dfs(i)

def bfs(V):
    queue = [V]
    visited[V] = 1

    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1,N+1):
            if(visited[i] == 0 and matrix[V][i] == 1):
                queue.append(i)
                visited[i] = 1

dfs(V)
visited = [0 for i in range(N+1)]
print()
bfs(V)