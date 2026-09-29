class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            profit = prices[i] - buy
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit