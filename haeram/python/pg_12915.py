def solution(strings, n):
    arr = []
    for s in strings:
        arr.append([s, s[n]])
    
    arr = sorted(arr, key=lambda x: (x[1], x[0]))
    
    ans = []
    for i in arr:
        ans.append(i[0])
    
    return ans


# 풀이 2
def solution(strings, n):
    ans = sorted(strings, key=lambda x: (x[n], x))
    
    return ans