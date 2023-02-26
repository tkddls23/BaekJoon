import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = collections.deque()
        s = s.lower()
        for i in s:
            if i.isalpha() or i.isnumeric():
                d.append(i)
        while len(d) > 1:
            if len(d) > 1 and d.popleft() != d.pop():
                return False
        return True

# 첫 번째 풀이
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         palindrome = ""
#         for i in s:
#             if i.isalpha() or i.isnumeric():
#                 palindrome += i
#         if palindrome == palindrome[::-1]:
#             return True
#         return False