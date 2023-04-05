# rotate image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 좌상단 대각선으로 뒤집기
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 각 행의 요소들을 교환하기
        for i in range(n):
            for j in range(n // 2): # 절반만 해도되기 때문
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

