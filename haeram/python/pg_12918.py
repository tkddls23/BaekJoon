def isLengthIs4or6(str):
    check = len(list(str))
    return True if (check == 4 or check == 6) else False
    

def solution(s):
    return isLengthIs4or6(s) and s.isdigit()
    


# 불필요한 연산을 모두 줄인 풀이법
def solution2(s):
    return len(s) in (4, 6) and s.isdigit()