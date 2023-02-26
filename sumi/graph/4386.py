import sys
import math

sys.stdin = open('index.txt')
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    n = int(input())

    arr = []
    for _ in range(n):
        a, b = map(float, input().strip().split())
        arr.append((a, b))

    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            cost = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

            edges.append((cost, i + 1, j + 1))
    edges.sort()
    total_cost = 0
    for i in range(len(edges)):
        cost, a, b = edges[i]

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost
    print("{:.2f}".format(total_cost))
