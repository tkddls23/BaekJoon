N = int(input())
result = 0

while N >= 0 :
    if N % 5 == 0 :
        result += int(N/5)
        print(result)
        break
    else:
        N -= 3
        result += 1

if N < 0 : 
    print("-1")
