import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = 0
        profit = 0
        
        for i in range(len(prices)):
                
            if prices[buy] > prices[i]:
                buy = i
                sell = i
                
            if prices[i] > prices[sell]:
                sell = i
                profit = max(profit,prices[sell]-prices[buy])
        
        return profit
        '''
        profit,buy = 0,prices[0]
        
        for num in prices:
            profit = max(profit,num-buy)
            buy = min(buy,num)
        
        return profit
        '''