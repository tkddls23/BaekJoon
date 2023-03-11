def solution(A, B):
    A.sort()
    B.sort()
    
    a_idx = 0
    b_idx = 0
    
    ans = 0
    while(a_idx < len(B) and b_idx < len(A)):
        if(A[a_idx] < B[b_idx]):
            ans += 1
            a_idx += 1
            b_idx += 1
        elif(A[a_idx] >= B[b_idx]):
            b_idx += 1
        
    return ans