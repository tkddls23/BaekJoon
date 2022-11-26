# 2630 색종이 만들기

def division(start_row, start_col, size):
    if size == 1:   # 픽셀 하나일 때
        result.append(arr[start_row][start_col])
        return
    num = arr[start_row][start_col]

    for row in range(start_row, start_row + size):
        for col in range(start_col, start_col + size):
            if num != arr[row][col]:
                size //= 2
                division(start_row, start_col, size)
                division(start_row, start_col + size, size)
                division(start_row + size, start_col, size)
                division(start_row + size, start_col + size, size)
                return

    result.append(arr[start_row][start_col])
    return


n = int(input())
arr = []
result = []
for _ in range(n):
    arr.append(list(map(int, list(input().split(" ")))))

division(0, 0, n)
print(result.count(0))
print(result.count(1))