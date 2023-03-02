import copy
import sys
input = sys.stdin.readline


def check_row_cnt(i, arr):
    max_cnt = 1
    cnt = 1
    for jdx in range(1, len(arr[i])):
        if arr[i][jdx - 1] == arr[i][jdx]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1

    return max(max_cnt, cnt)


def check_col_cnt(j, arr):
    max_cnt = 1
    cnt = 1
    for idx in range(1, len(arr)):
        if arr[idx - 1][j] == arr[idx][j]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    return max(max_cnt, cnt)


def check_cnt(x1, y1, x2, y2, arr):
    if x1 == x2:
        t1 = check_row_cnt(x1, arr)
        t2 = check_col_cnt(y1, arr)
        t3 = check_col_cnt(y2, arr)

        return max(t1, t2, t3)

    if y1 == y2:
        t1 = check_row_cnt(x1, arr)
        t2 = check_col_cnt(y1, arr)
        t3 = check_row_cnt(x2, arr)
        # print(arr)
        # print((x1, y1),( x2, y2),t1,t2,t3)
        return max(t1, t2, t3)


def bfs(arr, n):

    max_cnt = 1

    for i in range(n):
        for j in range(1, n):
            new_arr =  copy.deepcopy(arr)
            t = new_arr[i][j]
            new_arr[i][j] = new_arr[i][j - 1]
            new_arr[i][j - 1] = t
            res_cnt = check_cnt(i, j - 1, i, j,new_arr)
            max_cnt = max(max_cnt, res_cnt)

    for i in range(1,n):
        for j in range(n):
            new_arr = copy.deepcopy(arr)
            t = new_arr[i][j]
            new_arr[i][j] = new_arr[i -1][j]
            new_arr[i-1][j] = t
            res_cnt = check_cnt(i -1, j, i, j, new_arr)
            max_cnt = max(max_cnt, res_cnt)
            # print((i-1,j),(i,j),res_cnt)

    return max_cnt
if __name__ == '__main__':
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(list(input().strip()))
    res = 1
    for i in range(n):
        t1 = check_row_cnt(i, arr)
        t2 = check_col_cnt(i, arr)
        res = max(res, t1, t2)

    t = bfs(arr, n)
    print(max(res, t))