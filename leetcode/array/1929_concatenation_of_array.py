"""
Problem: 1929. Concatenation of Array
Link: https://leetcode.com/problems/concatenation-of-array/
Difficulty: Easy
"""


from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = nums + nums
        return k