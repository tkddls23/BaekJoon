def solution(picks, minerals):
    cnt = sum(picks)
    mine = [[0]*5 for _ in range(cnt)]

    trans = {k:v for k,v in zip(["diamond","iron","stone"],[25,5,1])}
    minerals = [trans[i] for i in minerals[:5*cnt]]

    for i,v in enumerate(minerals):
        N,i = i//5, i%5
        mine[N][i] = v    
    mine.sort(key=lambda x:-sum(x))

    picks = [25]*picks[0] + [5]*picks[1] + [1]*picks[2]
    result = 0
    for p,m in zip(picks,mine):
        result += sum([max(1,i//p) for i in m if i>0])
    return result

print(solution([1, 2, 3], ["diamond", "diamond", "diamond", "diamond", "stone", "iron", "iron", "iron", "iron", "iron", "diamond", "diamond", "diamond", "diamond", "diamond", "stone",
                           "diamond", "diamond", "diamond", "diamond", "stone",
                           "diamond", "diamond", "diamond", "diamond", "stone",
                           "diamond", "diamond", "diamond", "diamond", "stone",
                           "diamond", "diamond", "diamond", "diamond", "stone",]))