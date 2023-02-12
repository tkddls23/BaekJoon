def solution(sizes):
    bigs = []
    smalls = []
    
    for size in sizes:
        bigs.append(max(size[0], size[1]))
        smalls.append(min(size[0], size[1]))
        
    return max(bigs) * max(smalls)