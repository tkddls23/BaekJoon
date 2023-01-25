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


# 어떻게 이 풀이를 떠올렸지?
'''
맨 처음에 한 칸씩 밀어가면서 페어 스왑을 하면 원하는 결과를 얻을 수 있다는 사실을 발견함.
하지만 이 풀이는 O(n)에 풀 수 없어서 다른 풀이를 생각함.
even 노드를 하나 따로 만든다.
while 문을 돌며 even 은 even 노드에 물려주고 odd 는 odd 노드에 물려줌.
while 문을 빠져나와서 odd 노드에 even 노드를 물려준 후 반환함.

even 으로 관점을 바꾸고
변수명에 좀 더 신경을 썼으면 더 좋았을 것 같음.
'''
