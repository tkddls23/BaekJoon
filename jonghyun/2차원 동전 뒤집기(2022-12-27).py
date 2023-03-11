import copy


def filpHorizintal(binaryNum, begin, size):
    for i in range(0, len(binaryNum)):
        if int(binaryNum[i]) == 1 :
            for j in range(size) :
                if begin[i][j] == 1 :
                    begin[i][j] = 0
                else :
                    begin[i][j] = 1


def filpVertical(binaryNum, begin, size):
    for i in range(0, len(binaryNum)):
        if int(binaryNum[i]) == 1 :
            for j in range(size):
                if begin[j][i] == 1:
                    begin[j][i] = 0
                else:
                    begin[j][i] = 1

def checkEqual(flip2, target):
    if flip2 == target :
        return True
    return False


def solution(beginning, target):
    size = len(beginning)
    size2 = len(beginning[0])
    answer = -1
    for i in range(pow(2, size)) :
        binaryNumHorizin = format(i, 'b')
        binaryNumHorizin = binaryNumHorizin.zfill(size)
        beginCopy = [item[:] for item in beginning]
        filpHorizintal(binaryNumHorizin, beginCopy, size2)
        for j in range(pow(2, size2)):
            binaryNumVerti = format(j, 'b')
            binaryNumVerti = binaryNumVerti.zfill(size2)
            t = [item[:] for item in beginCopy]
            filpVertical(binaryNumVerti, t, size)
            if checkEqual(t, target) :
                temp = 0
                for b1 in binaryNumHorizin :
                    if int(b1) == 1 :
                        temp += 1
                for b2 in binaryNumVerti:
                    if int(b2) == 1:
                        temp += 1
                if answer == -1 :
                    answer = temp
                answer = min(answer,temp)

    return answer

print( solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]) )
