
arr = []
b = 0
def init() :
    global b
    m, n, b = list(map(int, input().split()))
    global arr
    for i in range(m) :
        arr.append(list(map(int, input().split())))


def get_cost(height, block):
    global arr
    time = 0
    for i in arr :
        for j in i :
            diff = height - j
            if diff > 0 :
                block -= diff
                time += diff
            elif diff < 0 :
                time += 2 * abs(diff)
                block += abs(diff)
            else:
                continue
    if block < 0 :
        return -1
    else:
        return [time, height]

def solution() :
    init()
    global arr
    answer = []

    for height in range(0, 257) :
        global b
        cost = get_cost(height, b)
        if cost  == -1 :
            continue
        answer.append(cost)
    answer = sorted(answer, key = lambda x : (x[0], -x[1]))
    print(answer[0][0], answer[0][1])

solution()