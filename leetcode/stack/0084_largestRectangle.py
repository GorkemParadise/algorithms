from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] >= heights[i]):
                hh = heights[stack.pop()]
                ww = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, hh * ww)
            stack.append(i)

        return max_area
    
sol = Solution()
ss = sol.largestRectangleArea([2,1,5,6,2,3])
print(ss)