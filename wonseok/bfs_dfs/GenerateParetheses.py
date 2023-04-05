# Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(result, comb, open, close):
            if close == n:
                result.append(comb)
            else: # 아래 if문들이 elif로 안되있어서 둘다 실행될수있는 경우도 있음 "(())()" 이런거
                if open>close: # 여는괄호가 닫는괄호보다 많으면 닫는 괄호 추가
                    dfs(result, comb + ')', open, close+1)
                if open <n: # 여는 괄호가 n개보다 적으면 여는 괄호 추가
                    dfs(result, comb + '(', open +1, close)
        result = []
        dfs(result, '', 0,0)
        return result

