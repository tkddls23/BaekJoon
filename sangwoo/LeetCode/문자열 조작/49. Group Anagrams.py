from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 정렬과 defaultdict 사용
        anagram = collections.defaultdict(list)

        for word in strs:
            # 정렬해서 같은 단어면 같은 그룹에 넣기
            sorted_word = ''.join(sorted(word))
            anagram[sorted_word].append(word)

        return list(anagram.values())


# 첫 시도
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # 정렬과 사전 사용
#         anagram = {}
#
#         for word in strs:
#             # 정렬해서 같은 단어면 같은 그룹에 넣기
#             sorted_word = ''.join(sorted(word))
#             if sorted_word in anagram:
#                 anagram[sorted_word].append(word)
#             else:
#                 anagram[sorted_word] = [word]
#
#         return list(anagram.values())


# 어떻게 이 풀이를 떠올렸지?
# 애너그램은 문자를 재배열하여 다른 뜻을 가진 문자로 바꾸는 것을 의미한다.
# 애너그램들을 정렬하면 모두 같은 문자가 된다.
# 딕셔너리를 이용해 정렬했을 때 같은 문자를 가지는 애너그램들을 저장한다.

# 더 좋은 방법은?
# defaultdict를 이용하여 if 조건문을 없앤다.
