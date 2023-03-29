class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs.pop(0)

        if(len(strs) == 0):
            return pre

        for str in strs:
            temp = ""
            
            for i in range(len(pre)):
                if(i >= len(str) or pre[i] != str[i]):
                    break

                temp += pre[i]

            pre = temp

        return pre