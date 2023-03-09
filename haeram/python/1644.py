from sys import stdin

n = int(stdin.readline())
arr = [0] * (n+1)
primes = []

# 0인 값들이 소수
def getPrimes(num):
    for i in range(2, num+1):
        if(arr[i]):
            continue

        for j in range(i*2, num+1, i):
            arr[j] = 1
    
    for i in range(2, num+1):
        if(not arr[i]):
            primes.append(i)
    

getPrimes(n)


# two pointer
part_sum = 0
end = 0
ans = 0

for start in range(len(primes)):
    while(part_sum < n and end < len(primes)):
        part_sum += primes[end]
        end += 1

    if(part_sum == n):
        ans += 1

    part_sum -= primes[start]

print(ans)
