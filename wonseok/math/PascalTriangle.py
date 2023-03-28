# pascal's triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        def pascal(num):
            tmp = []
            if num == 1:
                return [1]
            if num == 2:
                return [1,1]
            if num == 3:
                return [1,2,1]
            for i in range(num):
                if i != 0 and i != (num-1):
                    tmp.append(result[num-2][i-1]+result[num-2][i])
                else:
                    tmp.append(1)
            return tmp
        for i in range(numRows):
            result.append(pascal(i+1))
        return result
