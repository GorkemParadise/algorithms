"""
Problem: 494. Target Sum
Link: https://leetcode.com/problems/target-sum/
Difficulty: Medium
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)

        if target > total or (total - target) % 2 != 0:
            return 0

        s = (total - target) // 2

        dp = [0] * (s + 1)
        dp[0] = 1 

        for n in nums:
            for j in range(s, n - 1, -1): 
                dp[j] += dp[j - n]

        return dp[s]