# Best time to Buy And sell Stock
# 각 값을 순회하면서 제일 작게샀을때를 찾는다 (1->5)이렇게되면 1이됨
# 최대 이익을 계산함
class Solution:
    def maxProfit(self, prices):
        max_profit, min_buy = (0, float('inf'))
        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price - min_buy)
        return max_profit
