# first unique character
class Solution:
    def firstUniqChar(self, s: str) -> int:
        fre = {}
        for i in s:
            if i in fre:
                fre[i] += 1
            else:
                fre[i] = 1
        for i in s:
            if fre[i] == 1:
                return s.index(i)
        return -1