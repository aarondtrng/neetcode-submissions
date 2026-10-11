class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        height = 0
        end = len(heights)-1
        for start in range(len(heights)):
            width = end-start
            minimum = min(heights[start],heights[end])
            product = minimum * width
            area = product if product > area else area
        return area