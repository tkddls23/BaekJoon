# 2263 트리의 순회
from sys import stdin

n = int(stdin.readline())
in_order = list(map(int, stdin.readline().split()))
post_order = list(map(int, stdin.readline().split()))

# 후위 순회의 끝값이 중위 순회의 어디 인덱스에 위치한지 확인을 위해
# 중위 순회의 값들의 인덱스값을 저장
position = [0] * (n + 1)
for i in range(n):
    position[in_order[i]] = i


# 분할 정복 방식으로 전위 순회를 찾음
def preorder(in_start, in_end, post_start, post_end):
    # 재귀 종료 조건 (수렴)
    if (in_start > in_end) or (post_start > post_end):
        return

    # 후위 순회 결과의 끝이 (서브)트리의 루트임을 이용
    root = post_order[post_end]
    print(root, end=" ")

    # 중위 순회의 왼쪽 서브트리의 범위 = 시작인덱스 ~ (시작인덱스 + 왼쪽 서브트리의 노드 수 + 1)
    # 중위 순회의 오른쪽 서브트리의 범위 = (끝 인덱스 - 오른쪽 서브트리의 노드 수 + 1)~ 끝 인덱스
    left_count = position[root] - in_start
    right_count = in_end - position[root]

    # left, right로 나눠 분할 정복 방식으로 트리를 추적하여 전위 순회를 찾아냄
    preorder(in_start, in_start + left_count - 1, post_start, post_start + left_count - 1)  # 왼쪽 서브트리
    preorder(in_end - right_count + 1, in_end, post_end - right_count, post_end - 1)  # 오른쪽 서브트리
