# 12865 평범한 배낭
from sys import stdin

# 물건 개수, 최대 무게
num, max_weight = map(int, stdin.readline().split())
arr = [[0,0]]
d = [[0]*(max_weight+1) for _ in range(num+1)]

# 물건들 배열 생성
for i in range(num):
    arr.append(list(map(int, input().split())))

for i in range(1, num+1):
    for j in range(1, max_weight+1):
        w = arr[i][0]
        v = arr[i][1]
        
        # 배낭에 넣을수있는 무게가 넣을 물건보다 작으면 그냥 넣지않는다
        if j < w:
            d[i][j] = d[i-1][j]
        # 넣을 물건을 안넣은 상태와 넣을 물건의 무게 만큼 뺀 상태에서 가치를 더한것 중 최대값
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

# 최대 무게인 배낭이 가치는 최대 가치
print(d[num][max_weight])
