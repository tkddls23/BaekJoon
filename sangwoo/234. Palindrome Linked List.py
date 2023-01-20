from collections import deque
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        d = deque()

        if not head:
            return True

        node = head

        while node is not None:
            d.append(node.val)
            node = node.next

        while len(d) > 1:
            if d.popleft() != d.pop():
                return False

        return True
