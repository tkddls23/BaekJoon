d = []

for i in range(5001):
    d.append(0)

d[3] = 1
d[5] = 1

def dp(x):
    if(x<0) : return 5000
    if(x==3 or x==5) : return 1

    if( d[x] != 0): return d[x]
    d[x] = min(dp(x-3)+1, dp(x-5)+1)
    return d[x]

n = int(input())

for i in range(1, n+1) :
    dp(i)
    
if d[n] >= 4000 :
    print("-1") 
else: print(dp(n))