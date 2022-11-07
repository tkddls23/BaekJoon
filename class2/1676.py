# 1676 팩토리얼 0의 개수

N = int(input())
d = [0]*501
d[0],d[1] = 1,1
cnt=0

def fac(n):
    if n == 0:
        return d[0]
    if n == 1:
        return d[1]
    elif d[n] != 0:
        return d[n]
    d[n] = fac(n-1) * n
    return d[n]

result = list(map(int,str(fac(N))))

for i in result:
    if result.pop()==0:
        cnt+=1
    else:
        break

print(cnt)