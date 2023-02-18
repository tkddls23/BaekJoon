def add_progress(pro, speed):
    for i in range(len(pro)):
        pro[i] += speed[i]
        
    return pro, speed

def solution(progresses, speeds):
    answer = []
    cnt = 0
    
    while len(progresses):            
        if(progresses[0] >= 100):
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if(cnt > 0):
                answer.append(cnt)
                cnt = 0
            else:
                progresses, speeds = add_progress(progresses, speeds)

    answer.append(cnt)

    return answer
    