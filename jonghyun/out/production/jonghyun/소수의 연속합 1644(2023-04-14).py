import math

def solution():
    target_value = int(input())
    answer = 0
    arr = is_prime_num(4_000_000)
    prime_arr = []

    for i,v in enumerate(arr) :
        if v :
            prime_arr.append(i)

    i = 0
    j = 0
    sum_val = prime_arr[0]
    while i <= j :
        if sum_val == target_value :
            answer += 1
            j += 1
            if i >= len(prime_arr) - 1 or j >= len(prime_arr) - 1:
                break
            sum_val += prime_arr[j]
        if sum_val > target_value :
            sum_val -= prime_arr[i]
            if i > len(prime_arr) - 1 or j > len(prime_arr) - 1:
                break
            i += 1
        elif sum_val < target_value :
            j += 1
            if i > len(prime_arr) - 1 or j > len(prime_arr) - 1:
                break
            sum_val += prime_arr[j]

    print(answer)



def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1

    return arr
solution()