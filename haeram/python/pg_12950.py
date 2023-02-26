def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]
    
    for col in range(len(arr1)):
        for row in range(len(arr1[col])):
            answer[col][row] = arr1[col][row] + arr2[col][row]
    
    return answer