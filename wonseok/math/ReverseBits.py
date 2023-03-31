# Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1) # 왼쪽으로 옮기고 최하위 비트 구해서 넣기
            n >>= 1
        return(result)