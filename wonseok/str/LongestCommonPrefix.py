# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs):
        common = strs[0]

        for str in strs:
            tmp = ""
            for i in range(len(common)):
                if i >= len(str) or common[i] != str[i]:
                    break
                tmp += common[i]
            common = tmp

        return(common)