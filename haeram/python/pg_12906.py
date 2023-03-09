def solution(arr):
    answer = []
    
    prev = -1
    for i in arr:
        if(prev == i):
            continue
        else:
            prev = i
            answer.append(i)
    
    return answer