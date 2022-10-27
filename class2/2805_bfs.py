# 2805 나무 자르기
from sys import stdin 

N,M = map(int,stdin.readline().split())

trees = list(map(int,stdin.readline().split()))

first, last = 0, max(trees)

while first <= last:
    mid = (first + last) //2 
    cnt = 0

    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    if cnt >= M:
        first = mid +1
    else:
        last = mid -1

print(last)