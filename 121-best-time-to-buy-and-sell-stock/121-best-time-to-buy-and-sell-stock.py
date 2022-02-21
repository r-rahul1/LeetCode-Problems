import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,buy = 0,prices[0]
        
        for num in prices:
            profit = max(profit,num-buy)
            buy = min(buy,num)
        
        return profit