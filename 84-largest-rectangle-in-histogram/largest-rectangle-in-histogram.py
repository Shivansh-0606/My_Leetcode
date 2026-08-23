class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n+1):
            curr_height = 0 if i==n else heights[i]

            while stack and curr_height < heights[stack[-1]]:
                h = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area , h * width)

            stack.append(i)
        
        return max_area


