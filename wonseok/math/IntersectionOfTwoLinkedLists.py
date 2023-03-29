# 160 Intersection of Two Linked Lists

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        a = headA
        b = headB
        while a != b:
            # 교차하는게 있을때 까지 이동하는데 리스트 두개가 동시에 끝에 도달하면 상대의 머리로 리다이렉트
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a