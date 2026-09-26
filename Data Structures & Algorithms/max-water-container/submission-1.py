class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = l = 0
        r = len(heights)-1
        maxHeight = heights.index(max(heights))
        while l < r:
            width = r-l
            minimum = min(heights[l],heights[r])
            product = minimum * width
            area = product if product > area else area
            if minimum == heights[l] and l < maxHeight:
                l+=1
            else:
                r-=1
            
        return area