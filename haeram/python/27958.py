from itertools import product
from sys import stdin
import math
import copy

# inputs
n = int(stdin.readline())
k = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
bullets = list(map(int, stdin.readline().split()))

# 총알들이 가는 경우의 수
idx = [i for i in range(n)]
cands = list(product(idx, repeat=k))

ans = 0
for cand in cands:
    copy_arr = copy.deepcopy(arr)
    loop_score = 0 # 이번 경우의 수에서 얻은 점수
    partial_score = 0 # 표적 일부분 깨서 쌓인 점수

    for i in range(k): # 총알 개수만큼 반복
        row = cand[i]
        for j in range(n): # 한 줄에서 얻는 점수
            if(copy_arr[row][j] == 0):
                continue

            if(copy_arr[row][j] >= 10): # 보너스
                loop_score += copy_arr[row][j]
                copy_arr[row][j] = 0
                break

            if(copy_arr[row][j] <= bullets[i]): # 표적을 깰 수 있을 때
                loop_score += (copy_arr[row][j] + partial_score) # 점수 누적
                fragment = math.floor(copy_arr[row][j] / 4) # 표적 파편 값
                copy_arr[row][j] = 0 # 깬 표적은 0으로

                # row-1, row+1, j-1, j+1 업데이트
                if(row > 0 and copy_arr[row-1][j] == 0):
                    copy_arr[row-1][j] = fragment
                if(row < n-1 and copy_arr[row+1][j] == 0):
                    copy_arr[row+1][j] = fragment
                if(j > 0 and copy_arr[row][j-1] == 0):
                    copy_arr[row][j-1] = fragment
                if(j < n-1 and copy_arr[row][j+1] == 0):
                    copy_arr[row][j+1] = fragment

                partial_score = 0
                break

            if(copy_arr[row][j] > bullets[i]): # 표적 한번에 다 못깬 경우
                partial_score += bullets[i] # 총알 점수만큼 점수 누적
                copy_arr[row][j] -= bullets[i] # 점수 차감
                break

    # print('it', cand, loop_score)
    ans = max(ans, loop_score)

print(ans)



