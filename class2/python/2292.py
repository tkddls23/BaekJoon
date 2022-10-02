x = int(input())
a = 1

while True:
    if x==1:
        print("1")
        break
    elif x <= 3*a*(a+1) +1:
        print(a+1)
        break
    else:
        a+=1