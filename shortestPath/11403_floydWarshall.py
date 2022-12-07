# 11403 경로 찾기

n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

# 플로이드 워셜 알고리즘
for i in range(n):
    for j in range(n):
        for k in range(n):
            if matrix[j][k] == 1 or (matrix[j][i] == 1 and matrix[i][k] ==1):
                matrix[j][k] = 1

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()
