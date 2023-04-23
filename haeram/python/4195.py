# 시간 초과

# from sys import stdin

# t = int(stdin.readline())

# def find(x):
#     if parent[x] == x:
#         return x

#     parent[x] = find(parent[x])
#     return parent[x]

# def union(a, b):
#     a = find(a)
#     b = find(b)
        
#     if a<b:
#         parent[b] = a
#     else:
#         parent[a] = b


# for _ in range(t):
#     f = int(stdin.readline())
#     parent = [i for i in range(f+1)]
#     dict = {}
#     idx = 0

#     for _ in range(f):
#         f1, f2 = stdin.readline().split()
        
#         if f1 not in dict:
#             dict[f1] = idx
#             f1 = idx
#             idx += 1
#         else:
#             f1 = dict[f1]

#         if f2 not in dict:
#             dict[f2] = idx
#             f2= idx
#             idx += 1
#         else:
#             f2 = dict[f2]

#         prev1 = parent[f1]
#         prev2 = parent[f2]

#         union(f1, f2)

#         after1 = parent[f1]
#         after2 = parent[f2]

#         length = len(parent)
#         if prev1 != after1:
#             for i in range(length):
#                 if parent[i] == prev1:
#                     parent[i] = after1
                
#         if prev2 != after2:
#             for i in range(length):
#                 if parent[i] == prev2:
#                     parent[i] = after2

#         # print(f1, f2)
#         # print(parent)
#         print(parent.count(parent[f1]))

# ------------------------------------------------- #
from sys import stdin

t = int(stdin.readline().rstrip())

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
        
    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]


for _ in range(t):
    f = int(stdin.readline().rstrip())
    parent = {}
    cnt = {}

    for _ in range(f):
        f1, f2 = stdin.readline().split()
        
        if f1 not in parent:
            parent[f1] = f1
            cnt[f1] = 1

        if f2 not in parent:
            parent[f2] = f2
            cnt[f2] = 1

        union(f1, f2)

        ans1 = find(f1)
        # ans2 = find(f2)
        print(cnt[ans1])