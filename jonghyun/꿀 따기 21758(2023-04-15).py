def case1(sum_arr, arr):
    house_point = 0
    start_point1 = len(sum_arr) - 1

    v1 = sum_arr[start_point1] - arr[start_point1]

    max_val = 0
    for start_point2 in range(1, len(sum_arr) - 1):
        max_val = max(max_val, v1 - 2 * arr[start_point2] + sum_arr[start_point2])

    return max_val


def case2(sum_arr, arr):
    house = len(sum_arr) - 1
    start_point1 = 0
    v1 = sum_arr[house] - sum_arr[start_point1]

    max_val = 0
    for start_point2 in range(1, len(sum_arr) - 1):
        sum_arr[house] - sum_arr[start_point2]
        max_val = max(max_val, v1 + sum_arr[house] - sum_arr[start_point2] - arr[start_point2])
    return max_val


def case3(sum_arr, arr):
    start_point1 = 0
    start_point2 = len(sum_arr) - 1
    max_val = 0

    for house in range(1, len(sum_arr) - 1):
        max_val = max(max_val, sum_arr[-1] + arr[house] - arr[start_point1] - arr[start_point2])
    return max_val


def solution(N, arr):
    sum_arr = [0 for _ in range(len(arr))]

    for key, value in enumerate(arr):
        if key == 0:
            sum_arr[0] = value
        else:
            sum_arr[key] = sum_arr[key - 1] + value

    v1 = case1(sum_arr, arr)
    v2 = case2(sum_arr, arr)
    v3 = case3(sum_arr, arr)

    print(max(v1, v2, v3))


def init():
    N = int(input())
    arr = list(map(int, input().split()))
    solution(N, arr)


init()