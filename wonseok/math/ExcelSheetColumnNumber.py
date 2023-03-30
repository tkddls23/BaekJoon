# Excel Sheet Column Number
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def columnNumber(c):
            return (ord(c)-ord('A')+1)
        result = 0
        for i in range(len(columnTitle)):
            a = columnNumber(columnTitle[i])*(26**(len(columnTitle)-i-1))
            result += a
        return result