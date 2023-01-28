from collections import deque

# 첫 번째 풀이
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x: int) -> None:
        self.q1.append(x)
    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.popleft()
    def top(self) -> int:
        return self.q1[-1]
    def empty(self) -> bool:
        if self.q1:
            return False
        return True

# 두 번째 풀이
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# 문제 풀이
'''
파이썬의 리스트나 데크에서 제공하는 기능으로 쉽게 풀 수 있으나
큐의 기본연산만 써서 스택을 구현하는 문제의 취지에 맞게 풀었다.
첫 번째 풀이는 큐를 두개 이용해서 pop 을 할 때 마지막 요소가 나오기 전까지
다른 큐로 popleft 한 값을 append 해주고 마지막 요소를 popleft 해서 반환했다. 

두번째 풀이는 push 연산에서 요소를 넣을 때 
가장 마지막에 넣은 요소가 가장 앞으로 올 수 있도록 정렬했다. 
이를 통해 pop 연산을 할 때 popleft 로 바로 pop 할 수 있다. 
'''