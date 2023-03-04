from heapq import heappush, heappop

def solution(jobs):
    jobs.append([987654321, 0])
    heap = []
    sumTime = 0
    lastTime = 0
    for [time, length] in sorted(jobs, key = lambda x: (x[0], x[1])):
        if lastTime < time:
            if not heap:
                lastTime = time + length
                sumTime += lastTime - time
                continue
            while heap and lastTime < time:
                [popLength, popTime] = heappop(heap)
                lastTime += popLength
                sumTime += lastTime - popTime
        heappush(heap, [length, time])

    return int(sumTime / (len(jobs) - 1))

print(solution([[0, 3], [1, 9], [2, 6]]))