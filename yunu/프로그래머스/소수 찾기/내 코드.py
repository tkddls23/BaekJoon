def solution(n):
    numArr = [True for _ in range(n + 1)]
    priNums = []
    for num in range(2, n + 1):
        if numArr[num]:
            priNums.append(num)
            for nextNum in range(num, n + 1, num):
                numArr[nextNum] = False

    return len(priNums)