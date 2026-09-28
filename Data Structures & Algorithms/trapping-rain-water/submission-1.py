class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        suf = [0] * len(height)
        res = 0
        
        Max = 0
        for i in range(len(height)):
            currMax = height[i]
            Max = currMax if currMax > Max else Max
            pre.append(Max) 

        Max = 0
        for i in range(len(height)-1,-1,-1):
            currMax = height[i]
            Max = currMax if currMax > Max else Max
            suf[i] = Max 


        for i in range(len(height)):
            res += min(pre[i],suf[i]) - height[i]
        return res