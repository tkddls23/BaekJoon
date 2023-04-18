def solution(ft, k):
    answer = 0

    while k > 0 :
        a = k // (len(ft) - ft.count(0) )
        b = k % (len(ft) - ft.count(0) )

        for i, j in zip(ft, range(len(ft))):
            if ft[j] != 0:
                ft[j] = i - a
                if ft[j] < 0:
                    b = b + abs(ft[j])
                    ft[j] = 0
            k = b

        if len(ft) - ft.count(0) ==0:
            return -1

        if k+1 <= len(ft) - ft.count(0):
            for i in ft:
                answer += 1
                if i !=0 :
                    k -= 1
                if k == -1:
                    return answer