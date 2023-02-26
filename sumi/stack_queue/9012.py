import sys
from collections import deque

sys.stdin = open('index.txt')
input = sys.stdin.readline

def solution(arr):
    stack = deque()
    for x in arr:
        if x == '(':
            stack.append(x)
        else:
            if stack:
                stack.popleft()
            else:
                return False

    if stack:
        return False
    return True

if __name__ == "__main__":

    n= int(input())
    for _ in range(n):
        str = input().strip()
        res = solution(list(str))
        print('YES' if res else 'NO')

