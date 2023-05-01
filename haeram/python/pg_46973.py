import heapq

def solution(sequence, k):
    if sequence[0] == k:
        return [0, 0]
    
    end = 1
    length = len(sequence)
    
    hq = []
    cur_sum = sequence[0]
    for i in range(length):
        while (end < length and cur_sum < k):
            cur_sum += sequence[end]
            end += 1

        if cur_sum == k:
            heapq.heappush(hq, (end-i-1, i, end-1))

        cur_sum -= sequence[i]
    
    ans = heapq.heappop(hq)
    return [ans[1], ans[2]]