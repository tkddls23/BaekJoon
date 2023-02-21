def solution(triangle):
    max_len = len(triangle[-1])
    arr = [[0]*max_len for _ in range(max_len)]
    
    #initialize dp
    arr[0][0] = triangle[0][0]
    for i in range(1, max_len):
        arr[i][0] = arr[i-1][0] + triangle[i][0]
    
    for i in range(1, max_len):
        for j in range(1, i+1):
            arr[i][j] = triangle[i][j] + max(arr[i-1][j-1], arr[i-1][j])
    
    return max(arr[-1])
