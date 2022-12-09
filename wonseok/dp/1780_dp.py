# 1780 종이의 개수
# 9x9 => 3x3 => 1x1

# nxn 크기 지정
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

# 종이 종류 RESULT
result = {-1:0, 0:0,1:0}


def dp(row, col, n):
    current = matrix[row][col]

    for i in range(row, row+n):
        for j in range(col, col+n):
            # 현재 종이 종류와 다르다면
            if matrix[i][j] != current:
                # 종이 1/3로 분할 (ex. n == 9 , n = 9 -> 3 -> 1 )
                next = n//3
                # 종이를 같은 크기의 종이 9개로 자르므로
                dp(row, col, next) # 1번째 block (0,0)
                dp(row, col+next, next) # 2번째 block (0,1)
                dp(row, col+(next*2), next) # 3번째 block (0,2)
                dp(row+next, col, next) # 4번째 block (1,0)
                dp(row+next, col+next, next) # 5번째 block (1,1)
                dp(row+next, col+(next*2), next) # 6번째 block (1,2)
                dp(row+(next*2), col, next) # 7번째 block (1,0)
                dp(row+(next*2), col+next, next) # 8번째 block (1,1)
                dp(row+(next*2), col+(next*2), next) # 9번째 block (1,2)
                return
    result[current] +=1
    return

dp(0,0,n)

# 종이의 결과 출력
for i in result.values():
    print(i)