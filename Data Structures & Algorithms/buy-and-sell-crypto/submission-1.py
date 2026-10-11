class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = 0
        Min = float('inf')
        l = 0
        r = len(prices)-1

        while(l <= r):
            currMin = prices[l]
            currMax = prices[r]
            Min = currMin if currMin < Min else Min
            Max = currMax if currMax > Max else Max
            l+=1
            r-=1
        if Max - Min > 0:
            return Max-Min
        return 0
