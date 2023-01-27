from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        # 각 노드를 배열에 추가
        while head is not None:
            result.append(head)
            head = head.next
        # 뒤집는다.
        result.reverse()

        if result:
            answer = result[0]
            # 각 노드들을 연결
            for i in range(0, len(result)):
                if i == len(result) - 1:
                    result[i].next = None
                else:
                    result[i].next = result[i + 1]
            return answer
        else:
            return head


# 어떻게 이 풀이를 떠올렸지?
# 반대로 뒤집고 싶은데 연결리스트를 뒤집을 수는 없으니 이를 배열에 넣어서 하면 어떨까 하는 생각을 했다.
# 파이썬 배열에는 모든 자료형을 넣을 수 있기 때문에 순서대로 노드를 배열에 추가했다.
# 그리고 뒤집었다
# 뒤집은 후에 각 노드들은 연결한 후에 head를 반환했다.

# 더 좋은 풀이는 없을까?
# 연결 리스트 그 자체로 풀이하는 방법은 없을까?
# 재귀적으로 뒤집는 방법은??