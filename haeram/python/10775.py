# 시간 초과
# from sys import stdin

# g = int(stdin.readline())
# p = int(stdin.readline())
# visited = [0] * (g+1)

# planes = []
# for _ in range(p):
#     planes.append(int(stdin.readline()))

# ans = 0
# for plane in planes:
#     docked = False
    
#     for i in range(plane, 0, -1):
#         if not visited[i]:
#             visited[i] = 1
#             docked = True
#             break

#     if docked:
#         ans += 1
#     else:
#         break

# print(ans)

# ----------------------------------------------- #
from sys import stdin

def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX < rootY:
        parents[rootY] = parents[rootX]
    else:
        parents[rootX] = parents[rootY]


g = int(stdin.readline())
p = int(stdin.readline())
planes = [int(stdin.readline()) for _ in range(p)]
parents = [i for i in range(g+1)]

cnt = 0
for p in planes:
    root = find(p)

    if root == 0:
        break

    union(root, root-1)
    cnt += 1

print(cnt)
    
