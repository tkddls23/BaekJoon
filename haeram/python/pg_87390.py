def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        x = i//n
        y = i%n
        answer.append(max(x, y)+1)
        
    return answer