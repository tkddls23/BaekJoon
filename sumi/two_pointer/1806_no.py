import sys
import math

sys.stdin = open('index.txt')
input = sys.stdin.readline


def solution(preSum, n,s):
    for length in range(n):
        for idx in range(n-length):
            if idx == 0:
                temp = preSum[length + idx]
            else:
                temp = preSum[length+idx] - preSum[idx-1]
            if temp >= s:
                return length+1
    return 0
if __name__ == "__main__":
    n,s = map(int,input().split())

    arr = list(map(int, input().split()))

    preSum = [0] * n
    preSum[0] = arr[0]
    for i in range(1,len(arr)):
        preSum[i] = preSum[i-1] + arr[i]
    res = solution(preSum, n,s)

    print(res)