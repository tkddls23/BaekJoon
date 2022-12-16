# 17219 비밀번호 찾기
from sys import stdin

n, m = map(int,stdin.readline().split())
dic = {}
for i in range(n):
    domain, pwd = stdin.readline().split()
    dic[domain] = pwd

for j in range(m):
    domain = stdin.readline().strip()
    print(dic[domain])