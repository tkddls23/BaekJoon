import sys
input = sys.stdin.readline

def  solution(s):
    cnt = 0
    res = 0
    if s == 1:
        return 1
    for i in range(1,s+1):
        res += i
        cnt +=1
        if res == s:
            return cnt
        if res >= s:
            return (cnt -1)

if __name__ == "__main__":
    s = int(input().strip())

    res = solution(s)
    print(res)