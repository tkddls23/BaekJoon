def solution(arr1, arr2):
    col = len(arr1)
    row = len(arr2[0])
    
    answer = [[0]*row for _ in range(col)]
    
    for i in range(col):
        for j in range(row):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    
    return answer