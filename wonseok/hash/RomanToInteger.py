# RomanToInteger
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        prev = 0
        romanValues = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in s[::-1]:
            current = romanValues[i]
            if current < prev:
                result -= current
                continue
            result += current
            prev = current
        return result