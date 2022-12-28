def arrInit(arr):
    checkList = [50]
    for i in range(1,21) :
        arr[i] = [1, 1]
        arr[i * 2] = checkMin(arr[i * 2], [1, 0])
        arr[i * 3] = checkMin(arr[i * 3], [1, 0])
        checkList.extend([i, i*2, i*3])
    arr[50] = [1, 1]
    return checkList


def checkMin(param, param1):
    if param[0] < param1[0] :
        return param
    elif param[0] == param1[0] :
        if param[1] > param1[1] :
            return param
    return param1


def makeArr():
    arr = [[0xFFFFFF, 0] for _ in range(100100)]
    checkList = arrInit(arr)
    for i in range(20, 100010) :
        for j in checkList :
            arr[i] = checkMin([arr[i - j][0] + arr[j][0], arr[i - j][1] + arr[j][1]], arr[i])
    return arr


def solution(target):
    arr = makeArr()
    return arr[target]

solution(100)
