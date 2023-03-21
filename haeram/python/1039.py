from sys import stdin
import sys

n, k = stdin.readline().split()
k = int(k)

# if(k > len(n)):
#     print(-1)
#     sys.exit(0)

def swap(str, i, j):
    return str[0:i] + str[j] + str[i+1:j] + str[i] + str[j+1:len(str)]

changed_k = set()
changed_k.add(n)    

for z in range(k):
    temp = set()

    while changed_k:
        cur = changed_k.pop()

        for i in range(len(cur)):
            for j in range(i+1, len(cur)):
                if(i == 0 and cur[j] == '0'): #맨 처음에 0이 오면 큰일남
                    continue
                
                swapped = swap(cur, i, j)
                temp.add(swapped)

    changed_k = temp

if(not changed_k):
    print(-1)
else:
    print(int(max(changed_k)))

