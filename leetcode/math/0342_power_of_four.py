"""
Problem: 342. Power of Three
Link: https://leetcode.com/problems/power-of-four/
Difficulty: Easy
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 4 == 0:
            n = n // 4
        return n == 1