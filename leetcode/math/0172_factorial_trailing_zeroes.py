"""
Problem: 172. Factorial Trailing Zeroes
Link: https://leetcode.com/problems/factorial-trailing-zeroes/
Difficulty: Medium
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:

        five_counter = 0

        while n >= 5:
            five_counter += n // 5
            n = n // 5

        return five_counter
