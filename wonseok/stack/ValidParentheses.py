# Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        value = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in value.values():
                stack.append(char)
            if char in value.keys():
                if not stack or stack.pop() != value[char]:
                    return False
        return not stack

s = Solution()
print(s.isValid(input()))
