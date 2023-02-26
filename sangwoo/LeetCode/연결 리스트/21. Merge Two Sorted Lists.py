from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

# 문제 풀이
# 이미 두 연결 리스트는 정렬되어 있다.
# 두 노드 중에 작은 값을 왼쪽에 오도록 하고
# 다음 노드를 지금 노드의 다음 노드와 다른 노드 중에 작은 값으로 물려준다.
# 이를 위해 자기 자신을 호출한다.
