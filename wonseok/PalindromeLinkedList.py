# palindrome linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def pali(palindromeList):
            if palindromeList == palindromeList[::-1]:
                return True
            else:
                return False
        palindromeList = []
        while head != None:
            palindromeList.append(head.val)
            head = head.next

        return pali(palindromeList)

