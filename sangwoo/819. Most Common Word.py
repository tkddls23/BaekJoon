import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = ""

        for i in paragraph:
            # 대소문자를 구분하지 않는다.
            if i.isalnum():
                words += i.lower()
            # 구두점(마침표, 쉼표) 무시
            else:
                words += " "

        most = Counter(words.split()).most_common()

        # 금지된 단어에 포함 되지 않으면 해당 단어를 return
        for i in most:
            if i[0] not in banned:
                return i[0]

# 정규표현식 사용
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
#             .lower().split()
#                  if word not in banned]
#         counts = Counter(words)
#         return counts.most_common(1)[0][0]

# 첫 시도
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         result = []
#         strs = ""
#         # 구두점 무시
#         for i in paragraph:
#             if i.isalnum():
#                 strs += i.lower()
#             if i == "," or i == "." or i == " ":
#                 result.append(strs)
#                 strs = ""
#                 continue
#         if strs:
#             result.append(strs)
#         while '' in result:
#             result.remove('')
#
#         most = Counter(result).most_common()
#
#         for i in most:
#             if i[0] not in banned:
#                 return i[0]
