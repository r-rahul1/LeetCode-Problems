class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = 0
        profit = 0
        profitsum = 0
        
        for i in range(len(prices)):
            if prices[i] < prices[sell]:
                buy = i
                sell = i
                profitsum += profit
                profit = 0
            
            if prices[sell] < prices[i]:
                sell = i
                profit = prices[sell] - prices[buy]
        
        return profitsum+profit