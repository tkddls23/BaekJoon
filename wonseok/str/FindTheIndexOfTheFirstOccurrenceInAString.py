# Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

s = Solution()
print(s.strStr("leetcode", "leeto"))