# 1918 후위 표기식
from sys import stdin
from collections import deque

infix = stdin.readline().strip()
priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
stack = []
result = []


def convert_to_postfix(infix):
    for token in infix:
        if token.isupper():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and priority[token] <= priority[stack[-1]]:
                result.append(stack.pop())
            stack.append(token)
    while stack:
        result.append(stack.pop())
    return ''.join(result)


print(convert_to_postfix(infix))
