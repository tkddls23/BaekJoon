# 15289 Hashing
import sys
L = int(sys.stdin.readline())
str = input()

def power(x,y):
    if y == 0:
        return 1
    
    divide = power(x,y//2)

    if y%2==0:
        return divide * divide
    else:
        return divide * divide * x

result = 0
for i in range(len(str)):
    result += (ord(str[i])-ord('a')+1)*power(31,i)

print(result%1234567891)
