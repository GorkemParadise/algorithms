"""
Problem: Two Sum
Link: https://neetcode.io/problems/two-integer-sum/question?list=neetcode150
Difficulty: Easy
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nowhereingo = {}

        for i, v in enumerate(nums):
            bluelock = target - v
            if bluelock in nowhereingo:
                return [nowhereingo[bluelock],i]
            nowhereingo[v] = i