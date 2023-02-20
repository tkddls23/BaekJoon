import sys
input = sys.stdin.readline

def solution(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(0,i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)
if __name__ == "__main__":
    n = input()
    arr = list(map(int, input().split()))
    res = solution(arr)
    print(res)