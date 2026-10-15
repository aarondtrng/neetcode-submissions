class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxRec = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                heightIndex = stack.pop()
                height = heights[heightIndex]
                width = i if not stack else i - stack[-1] - 1
                maxRec = max(maxRec, height * width)
            stack.append(i)

        while stack:
            heightIndex = stack.pop()
            height = heights[heightIndex]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            maxRec = max(maxRec, height * width)

        return maxRec