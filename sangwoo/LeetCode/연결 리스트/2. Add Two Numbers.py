from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sums = []
        sum = 0
        while l1 and l2:
            sum += l1.val + l2.val
            # sum 이 10을 넘어가면
            if sum >= 10:
                node = ListNode(sum % 10)
                sums.append(node)
                # 올림
                sum = 1
            else:
                node = ListNode(sum)
                sums.append(node)
                sum = 0
            l1, l2 = l1.next, l2.next

        if l1:
            while l1:
                sum += l1.val
                if sum >= 10:
                    node = ListNode(sum % 10)
                    sums.append(node)
                    # 올림
                    sum = 1
                else:
                    node = ListNode(sum)
                    sums.append(node)
                    sum = 0
                l1 = l1.next
        if l2:
            while l2:
                sum += l2.val
                if sum >= 10:
                    node = ListNode(sum % 10)
                    sums.append(node)
                    # 올림
                    sum = 1
                else:
                    node = ListNode(sum)
                    sums.append(node)
                    sum = 0
                l2 = l2.next
        if sum:
            node = ListNode(sum)
            sums.append(node)

        answer = sums[0]
        for i in range(len(sums)):
            if i == len(sums) - 1:
                sums[i].next = None
            else:
                sums[i].next = sums[i + 1]

        return answer
