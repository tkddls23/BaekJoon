import sys

arr_len = 0

def binary_search(arr, value, index):
    global arr_len
    start = 0
    end = arr_len - 1
    while start <= end :
        mid = (start + end) // 2
        if arr[mid][1] == value :
            if arr[mid][0] == index :
                val1 = [0, sys.maxsize]
                val2 = [0, sys.maxsize]
                if mid + 1 < arr_len :
                    val1 = arr[mid + 1]
                if mid - 1 >= 0 :
                    val2 = arr[mid - 1]
                return min(abs(val1[1] - value), abs(val2[1] - value))
            else :
                return 0
        elif arr[mid][1] < value :
            start = mid + 1
        else :
            end = mid - 1



def solution(N, arr):
    global arr_len
    arr_len = len(arr)
    x_arr = [[key, value[0]] for key, value in enumerate(arr)]
    y_arr = [[key, value[1]] for key, value in enumerate(arr)]
    z_arr = [[key, value[2]] for key, value in enumerate(arr)]
    x_arr.sort(key= lambda v : v[1])
    y_arr.sort(key= lambda v : v[1])
    z_arr.sort(key= lambda v : v[1])
    print(x_arr, y_arr, z_arr)
    answer = 0
    index = 0
    for x, y, z in arr:
        x_min = binary_search(x_arr, x, index)
        y_min = binary_search(y_arr, y, index)
        z_min = binary_search(z_arr, z, index)
        answer += min(x_min, y_min, z_min)
        index += 1
    print(answer)


def init():
    arr = []
    N = int(input())
    for i in range(N):
        arr.append(list(map(int, input().split())))
    solution(N, arr)


solution(5, [[11, -15, -15], [14, -5, -15], [-1, -1, -5], [10, -4, -1], [19, -4, 19]])
