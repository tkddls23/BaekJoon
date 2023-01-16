import sys

sys.stdin = open('index.txt')
input = sys.stdin.readline

def main(n,arr):
    res = []
    current = (arr[0][0], arr[0][1])
    for start, end in arr:
        if current[1] < start: #안이어진경우
            res.append(current)
            current = (start,end)
        else:
            # 이어진 경우
            if current[1] < end:
                current = (current[0],end)


    res.append(current)
    answer = 0
    for start, end in res:
        answer += end - start
    return answer

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        t = list(map(int, input().split()))
        # t.sort()
        arr.append(t)

    arr.sort(key=lambda x:x[0])
    print(main(n,arr))
