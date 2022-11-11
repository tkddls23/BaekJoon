# 2164 카드2
import sys, math

N = int(sys.stdin.readline())

x = math.floor(math.log2(N))
tmp = 2**x
result = 2*(N - tmp)

if N == 1:
    print("1")
elif N==2:
    print("2")
else:
    if result == 0:
        print(N)
    else:
        print(result)
