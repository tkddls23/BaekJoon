from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 노드 값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(올림)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


# 처음 풀이
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         sums = []
#         sum = 0
#         while l1 and l2:
#             sum += l1.val + l2.val
#             # sum 이 10을 넘어가면
#             if sum >= 10:
#                 node = ListNode(sum % 10)
#                 sums.append(node)
#                 # 올림
#                 sum = 1
#             else:
#                 node = ListNode(sum)
#                 sums.append(node)
#                 sum = 0
#             l1, l2 = l1.next, l2.next
#
#         if l1:
#             while l1:
#                 sum += l1.val
#                 if sum >= 10:
#                     node = ListNode(sum % 10)
#                     sums.append(node)
#                     # 올림
#                     sum = 1
#                 else:
#                     node = ListNode(sum)
#                     sums.append(node)
#                     sum = 0
#                 l1 = l1.next
#         if l2:
#             while l2:
#                 sum += l2.val
#                 if sum >= 10:
#                     node = ListNode(sum % 10)
#                     sums.append(node)
#                     # 올림
#                     sum = 1
#                 else:
#                     node = ListNode(sum)
#                     sums.append(node)
#                     sum = 0
#                 l2 = l2.next
#         if sum:
#             node = ListNode(sum)
#             sums.append(node)
#
#         answer = sums[0]
#         for i in range(len(sums)):
#             if i == len(sums) - 1:
#                 sums[i].next = None
#             else:
#                 sums[i].next = sums[i + 1]
#
#         return answer


# 문제 풀이
'''
l1과 l2 중 하나가 None이 될 때까지 값을 더해간다.
이때 값은 sum 변수에 더해준다.
sum 변수를 val로 해서 새로운 node를 만들어 sums 리스트에 추가해준다.
이때 sum이 10보다 크다면 sum을 10으로 나눈 나머지를 val로 하여 node를 만든다.
sum의 초깃값은 0이지만 두 값의 합이 10보다 크다면 올림을 위해 sum에 1을 저장해준다.

둘 중 하나가 None이면 남은 연결 리스트를 위와 같은 방식으로(올림값 때문에 10을 넘을 수도 있으므로) sums 리스트에 추가한다.
마지막에 sum 이 1이라면 이 또한 1을 val로 하는 새로운 node를 만들어 sums 리스트에 추가한다
이 노드들을 모두 연결해준 후에 리턴한다.
'''

# 더 좋은 방법은 없을까?
'''
별도의 리스트를 사용하지 않고 바로 더해나가기 
'''

# 별도의 리스트를 사용하지 않고 바로 더해나가기
# 풀다가 실패한 풀이 -> 바로 더 하는 걸 기존 리스트에 하지말고 새로운 연결 리스트를 만들었으면 어떘을까
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         sum = 0
#         head = l1
#         while l1 and l2:
#             sum += l1.val + l2.val
#             # sum 이 10을 넘어가면
#             if sum >= 10:
#                 l1.val = sum % 10
#                 # 올림
#                 sum = 1
#             else:
#                 l1.val = sum
#                 sum = 0
#             l1, l2 = l1.next, l2.next
#
#         if l1:
#             while l1:
#                 sum += l1.val
#                 if sum >= 10:
#                     l1.val = sum % 10
#                     # 올림
#                     sum = 1
#                 else:
#                     l1.val = sum
#                     sum = 0
#                 l1 = l1.next
#         # l1 에 l2연결
#         if l2:
#             while l2:
#                 sum += l2.val
#                 if sum >= 10:
#                     l1.next = ListNode(sum % 10)
#                     # 올림
#                     sum = 1
#                 else:
#                     l1.next = ListNode(sum)
#                     sum = 0
#                 l1, l2 = l1.next, l2.next
#         if sum:
#             l1 = l1.next
#
#         return head
