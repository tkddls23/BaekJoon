# merge Two Lists
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val < list2.val:
                list1.next = merge(list1.next, list2) # 이어 붙이기
                return list1
            if list1.val >= list2.val:
                list2.next = merge(list1, list2.next) # 이어 붙이기
                return list2
        return merge(list1,list2)