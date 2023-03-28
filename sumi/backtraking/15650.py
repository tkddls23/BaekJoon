import sys
from itertools import product

sys.stdin = open('index.txt')
input = sys.stdin.readline




if __name__ == '__main__':

    n, m =  map(int, input().split())

    s = []

    def dfs():
        # 원하는 길이의 숫자 조합을 가졌을 때, 결과값을 출력
        if len(s) == m:
            print(' '.join(map(str, s)))
            return
        # 1부터 리스트에 추가했다가 다시 제거하기 때문에
        # 오름차순으로 리스트에 추가될 수 밖에 없다.
        # 고른 순열은 오름차순 이여야 한다.
        for i in range(1,n+1):
            if i not in s:
                if len(s)>0 and s[-1] > i:
                    continue
                s.append(i)
                dfs()
                s.pop()

    dfs()
