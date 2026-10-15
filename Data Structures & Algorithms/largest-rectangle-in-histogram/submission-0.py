class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxRec = 0 
        currMin = heights[0]
        for i in range(len(heights)):
            maxRec = max(maxRec, heights[i])
            while stack and stack[-1] > heights[i]:
                width = i - stack.pop(0)
                area = width * heights[i]
                maxRec = max(maxRec, area)
            stack.append(i)
        return maxRec