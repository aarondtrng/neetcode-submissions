class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            buy = prices[i] if prices[i] < buy else buy
            profit = prices[i] - buy
            maxProfit = profit if profit > maxProfit else maxProfit
        return maxProfit