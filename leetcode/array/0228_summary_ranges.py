"""
Problem: 228. Summary Ranges
Link: https://leetcode.com/problems/summary-ranges/
Difficulty: Easy
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            S = nums[i]

            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1

            if S != nums[i]:
                ans.append(f"{S}->{nums[i]}")
            else:
                ans.append(str(S))
            
            i += 1
        return ans
