# 18870 좌표 압축

n = int(input())

x_list = list(map(int,input().split(" ")))
x_set = sorted(list(set(x_list)))
x_map = {x_set[i] : i for i in range(len(x_set))}

for i in x_list:
    print(x_map[i], end=" ")