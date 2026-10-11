class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(len(height)):
            lMax = max(height[:i+1])
            rMax = max(height[i:])
            minimum = min(lMax,rMax)
            water = minimum - height[i]
            total+= water if water > 0 else 0
        return total
