def solution(a):
    dic = {}
    check = {}
    for i in range(len(a)):
        dic[i] = 0
        check[i] = -2

    for i in range(len(a) - 1):
        if a[i] != a[i+1]:
            if check[a[i]] != i-1:
                dic[a[i]] += 1
                check[a[i]] = i
            if check[a[i+1]] != i-1:
                dic[a[i+1]] += 1
                check[a[i+1]] = i

    return max(dic.values()) * 2

# print(solution([0]))
print(solution([5, 2, 3, 3, 5, 3]))
print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))