# 1967 트리의 지름
import sys

sys.setrecursionlimit(100000)

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):  # 노드 n개인 이진트리의 간선의 개수는 n-1
    u, v, w = map(int, input().split())
    tree[u].append([v, w])
    tree[v].append([u, w])


# 해당 노드에서 가장 먼 노드와 길이 구하기
def dfs(node, parent):
    max_node, max_dist = node, 0
    for neighbor, weight in tree[node]:
        if neighbor != parent:  # 이전 노드 빼고
            neighbor_node, neighbor_dist = dfs(neighbor, node)  # dfs로 인접 노드랑 길이 찾음
            neighbor_dist += weight
            if neighbor_dist > max_dist:
                max_node, max_dist = neighbor_node, neighbor_dist
    return max_node, max_dist


# 루트 노드에서 제일 먼 노드를 dfs로 구하고 그 노드에서 가장 먼 노드를 구한다
first_node, _ = dfs(1, 0)
second_node, diameter = dfs(first_node, 0)

print(diameter)
