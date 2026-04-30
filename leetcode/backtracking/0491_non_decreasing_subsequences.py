"""
Problem: 491. Non-decreasing Subsequences
Link: https://leetcode.com/problems/non-decreasing-subsequences/
Difficulty: Medium
"""


class Solution:
    def findSubsequences(self, nums):
        ans = []

        def backtrack(start, p):
            if len(p) >= 2:
                ans.append(p[:])  # add copy

            used = set()  # no duplicate

            for i in range(start, len(nums)):
                # non-decreasing
                if (p and nums[i] < p[-1]) or nums[i] in used:
                    continue

                used.add(nums[i])
                p.append(nums[i])

                backtrack(i + 1, p)

                p.pop()  # clear term

        backtrack(0, [])
        return ans