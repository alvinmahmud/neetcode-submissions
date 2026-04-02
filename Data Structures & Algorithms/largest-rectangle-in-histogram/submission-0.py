class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                res = max(res, heights[index] * width)
            stack.append(i)
        
        while stack:
            index = stack.pop()
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            res = max(res, heights[index] * width)

        return res
