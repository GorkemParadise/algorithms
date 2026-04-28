"""
Problem: 29. Divide Two Integers
Link: https://leetcode.com/problems/divide-two-integers/
Difficulty: Medium
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0):
            sign = -1
        else:
            sign = 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = dividend // divisor
        if sign == -1:
            return -1 * result

        min_limit = -(2 ** 31) 
        max_limit = (2 ** 31 - 1)

        return min(max(result, min_limit), max_limit)