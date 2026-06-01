"""
Problem: 1486. XOR Operation in an Array
Link: https://leetcode.com/problems/xor-operation-in-an-array/
Difficulty: Easy
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n == 1:
            return start
        return start ^ self.xorOperation(n - 1, start + 2)