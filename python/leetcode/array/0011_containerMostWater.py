class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxA = 0
        while left < right:
            maxA = max(maxA, (right-left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxA
    
sol = Solution()
ans = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(ans)  


"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Input: height = [1,1]
Output: 1
"""