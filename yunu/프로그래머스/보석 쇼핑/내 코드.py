from collections import defaultdict

def solution(gems):
    n = len(gems)
    totalType = len(set(gems))
    currType = defaultdict(int)
    interval = []
    
    end = 0
    for start in range(n):
        while len(currType) < totalType and end < n:
            currType[gems[end]] += 1
            end += 1
        
        if len(currType) == totalType:
            interval.append([start + 1, end])
            
        currType[gems[start]] -= 1
        if currType[gems[start]] == 0:
            del currType[gems[start]]
            
    return min(interval, key=lambda inter: inter[1] - inter[0])
