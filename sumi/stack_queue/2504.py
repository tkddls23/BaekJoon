import sys
from collections import deque

input = sys.stdin.readline


def solution(arr):
    stack = deque()
    temp = 1
    result = 0

    for idx in range(len(arr)):
        x = arr[idx]
        if x == '(':
            stack.append(x)
            temp *= 2
            continue
        if x == '[':
            stack.append(x)
            temp *= 3
            continue
        if idx == 0:
            return 0
        if not stack:
            return 0
        if x == ')':
            top = stack.pop()
            if top == '(':
                if arr[idx-1] == '(':
                    # 애기 괄호  ()
                    result += temp
                temp /=2
            else:
                return 0
        if x == ']':
            top = stack.pop()
            if top == '[':
                if arr[idx-1] == '[':
                    # 애기 괄호  ()
                    result += temp
                temp /=3
            else:
                return 0

    if stack:
        return 0
    return int(result)


if __name__ == "__main__":
    res = solution(list(input().strip()))
    print(res)
