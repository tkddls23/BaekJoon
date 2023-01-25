from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 첫 풀이
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        # 짝수번째 연결리스트
        even_root = even = head.next
        root = head
        while head and head.next and head.next.next:
            head.next = head.next.next
            head = head.next

            even.next = head.next
            even = even.next

        # 홀수 노드의 마지막에 짝수 헤드를 연결
        head.next = even_root
        return root
