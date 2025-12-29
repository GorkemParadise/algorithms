class Solution:
    def heightChecker(self, heights):
        excepted = sorted(heights)
        ans = 0
        hm = len(heights)
        for n in range(0, hm):
            if excepted[n] != heights[n]:
                ans += 1
        return ans
        

sol = Solution()
mm = sol.heightChecker([1,1,4,2,1,3])
print(mm)




'''
Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.
Example 3:

Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
'''