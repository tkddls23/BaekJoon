# reverse linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = None
        while first != None:
            nextNode = first.next
            first.next = second
            second = first
            first = nextNode
        return(second)