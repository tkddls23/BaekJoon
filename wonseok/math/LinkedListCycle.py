# linked list cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 중요한건 하나는 2칸 하나는 1칸 이동해서 서로 결국 사이클이 있으면 만날텐데 그걸 판별

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        first = head
        second = head
        while first != None and first.next != None:
            first = first.next.next
            second = second.next
            if first == second:
                print(first.val)
                print(second.val)
                return True
        return False