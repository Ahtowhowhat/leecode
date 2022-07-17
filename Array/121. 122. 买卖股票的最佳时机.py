from typing import List

# 121. 买卖股票的最佳时机
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            maxprofit = max(maxprofit, price - minprice)
            minprice = min(minprice, price)
        return maxprofit

# 122. 买卖股票的最佳时机 II
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dif = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        return sum([x for x in dif if x>0])