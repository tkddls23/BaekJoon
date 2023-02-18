def solution(s):
    arr = s[2:-2]
    arr = arr.split("},{")
    
    arr.sort(key=len)

    answer = []
    for a in arr:
        temp = a.split(',')
        for i in temp:
            if (int(i) not in answer):
                answer.append(int(i))
    
    return answer