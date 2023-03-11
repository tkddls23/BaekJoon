def convertToBaseN(num, base):
    res = []
    while (num):
        res.append(num % base)
        num = num // base
    
    return "".join(map(str, res)) #join은 str만 가능!

def solution(n):
    base3 = convertToBaseN(n, 3)
    return int(base3, 3)


# 좀 더 깔끔한 버전
def convertToBaseN(num, base):
    res = ''
    while (num):
        res += str(num % base)
        num = num // base

    return res

def solution(n):
    base3 = convertToBaseN(n, 3)
    return int(base3, 3)