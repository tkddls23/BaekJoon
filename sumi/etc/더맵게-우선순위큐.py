from queue import PriorityQueue

# 우선순위 큐의 push 함수의 시간복잡도가 O(n)이라서 시간초과가 뜨는 것 같다.

def solution(scoville, K):
    que = PriorityQueue()

    for x in scoville:
        que.put(x)

    cnt = 0
    while True:
        t = que.get()
        if t > K:
            return cnt

        if que.empty():
            return -1

        cnt += 1
        t2 = que.get()
        new_t = t + (t2 * 2)
        que.put(new_t)

