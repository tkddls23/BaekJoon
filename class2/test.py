while True:
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
    elif n > m:
        print(Yes)
    else:
        print(No)