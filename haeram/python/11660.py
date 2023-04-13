from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

# get partial sum
psum = [[0]*n for _ in range(n)]

# 누적합 초기값
for i in range(n):
    psum[i][0] = arr[i][0]

# 가로 방향 누적
for i in range(n):
  for j in range(1, n):      
      psum[i][j] = psum[i][j-1] + arr[i][j]

# 세로 방향 누적
for i in range(1, n):
    for j in range(n):
        psum[i][j] = psum[i-1][j] + psum[i][j]

# 정답 구하기
for i in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

    ans = 0
    if(x1 == 0 and y1 == 0):
        ans = psum[x2][y2]
    elif(x1 == 0):
        ans = psum[x2][y2] - psum[x2][y1-1]
    elif(y1 == 0):
        ans = psum[x2][y2] - psum[x1-1][y2]
    else:
        ans = psum[x2][y2] - psum[x2][y1-1] - psum[x1-1][y2] + psum[x1-1][y1-1]

    # print(ans)

for p in psum:
    print(p)