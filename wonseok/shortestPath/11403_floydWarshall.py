# 11403 경로 찾기

n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

# 플로이드 워셜 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 or (matrix[i][k] == 1 and matrix[k][j] ==1):
                matrix[i][j] = 1

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()
