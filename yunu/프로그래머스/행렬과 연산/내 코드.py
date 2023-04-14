from collections import deque

def solution(rc, operations):
    top = deque(rc[0])
    bottom = deque(rc[len(rc) - 1])
    left = deque()
    right = deque()
    middle = deque()
    for i in range(1, len(rc) - 1):
        left.append(rc[i][0])
        right.append(rc[i][-1])
        middle.append(rc[i][1:-1])
    
    for oper in operations:
        if oper == "ShiftRow":
            if len(left) > 0:
                temp = bottom
                bottom = deque([left.pop()] + middle.pop() + [right.pop()])
                left.appendleft(top.popleft())
                right.appendleft(top.pop())
                middle.appendleft(list(top))
                top = temp
            else:
                top, bottom = bottom, top
        else:
            if len(left) > 0:
                top.appendleft(left.popleft())
                right.appendleft(top.pop())
                bottom.append(right.pop())
                left.append(bottom.popleft())
            else:
                top.appendleft(bottom.popleft())
                bottom.append(top.pop())
    
    answer = []
    answer.append(list(top))
    for i in range(1, len(rc) - 1):
        answer.append([left.popleft()] + middle.popleft() + [right.popleft()])
    answer.append(list(bottom))
    return answer

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
print(solution([[1, 2], [3, 4]], ["Rotate", "ShiftRow", "ShiftRow"]))