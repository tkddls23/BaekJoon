# 시간 초과

def solution(sequence, k):
    length = len(sequence)
    ep = 0
    psum = [0] * length
    psum[0] = sequence[0]
    
    for i in range(1, length):
        psum[i] = psum[i-1] + sequence[i]
    
    cands = []
    for i in range(length):
        if psum[i] < k:
            continue
        elif psum[i] == k:
            cands.append([0, i, i])
            
        for j in range(i):
            if psum[i] - psum[j] < k:
                break
                
            if psum[i] - psum[j] == k:
                cands.append([j+1, i, i-j]) #start, end, length
            
    cands.sort(key=lambda x: (x[2], x[0]))
    
    return [cands[0][0], cands[0][1]]

# --------------------------------------------------------------------- #

