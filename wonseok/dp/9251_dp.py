# 9251 LCS
from sys import stdin

# n = int(stdin.readline())
# a = list(map(int, stdin.readline().split()))

str1 = list(input())
str2 = list(input())

d = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

# 같은 알파벳일때는 현재 lcs +1 다른 알파벳이면 현재까지 값들 비교
def dp():
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                d[i+1][j+1] = d[i][j]+1
                continue
            d[i+1][j+1] = max(d[i+1][j], d[i][j+1])
            print(d[i+1][j+1])

    return d[-1][-1]


print(dp())