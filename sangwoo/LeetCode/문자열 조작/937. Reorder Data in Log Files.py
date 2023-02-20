from typing import List

# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         letter_logs = []
#         digit_logs = []
#
#         # 로그들을 공백문자를 기준으로 분리
#         for i in logs:
#             log = i.split()
#             # 숫자 로그라면 입력 순서 보장하기 위해 따로 분리
#             if log[1].isnumeric():
#                 digit_logs.append(log)
#                 continue
#             letter_logs.append(log)
#         # x[1:], 1 이후부터 정렬 후에 같다면 식별자로 정렬
#         letter_logs.sort(key=lambda x: (x[1:], x[0]))
#
#         result = letter_logs + digit_logs
#         answer = []
#
#         for i in result:
#             answer.append(' '.join(i))
#
#         return answer

# 두번째 풀이
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        # 로그들을 공백문자를 기준으로 분리
        for i in logs:
            log = i.split()
            # 숫자 로그라면 입력 순서 보장하기 위해 따로 분리
            if i.split()[1].isdigit():
                digit_logs.append(i)
                continue
            letter_logs.append(i)
        # x[1:], 1 이후부터 정렬 후에 같다면 식별자로 정렬
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_logs + digit_logs
