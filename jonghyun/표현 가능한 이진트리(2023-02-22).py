global answer

def convertNumToBinaryStr(number):
    binaryNum = bin(number)
    split = binaryNum.split("b")
    numStr = split[1]

    while (len(numStr) in [1, 3, 7, 15, 31, 63, 127]) is False:
        numStr = '0' + numStr
    return 'X' + numStr


def preorder_traversal(index, depth, binary_str):
    if index < 1 or index >= len(binary_str) or depth == 1 :
        return binary_str[index]

    left = preorder_traversal(index - depth // 2, depth // 2, binary_str)
    right = preorder_traversal(index + depth // 2, depth // 2, binary_str)
    if binary_str[index] == '0' and (left == '1' or right == '1'):
        global answer
        answer = 0

    if binary_str[index] == '0':
        return '0'
    else :
        return '1'


def checkBinaryStr(binary_str):
    start_point = len(binary_str) // 2
    depth = start_point
    preorder_traversal(start_point, depth, binary_str)



def solution(numbers):
    answers = []

    for number in numbers:
        global answer
        answer = 1
        binary_str = convertNumToBinaryStr(number)
        # print(binary_str)
        checkBinaryStr(binary_str)

        # print(answer)
        if answer:
            answers.append(1)
        else:
            answers.append(0)

    return answers


# solution([5])
# solution([7, 42, 5])
# solution([63, 111, 95])
solution([31] )
# solution([31,63,127,256,511,1023])
