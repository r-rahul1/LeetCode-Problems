class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        p = 0
        
        for sell in range(len(prices)):
            if sell+1 < len(prices) and prices[sell] > prices[sell+1]:
                p += prices[sell]-prices[buy]
                buy = sell+1
        
        #if prices[-1] > prices[-2]:
        return p + (prices[-1]-prices[buy])
        
        #return p