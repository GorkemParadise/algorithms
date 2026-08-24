"""
Problem: 2485. Find the Pivot Integer
Link: https://leetcode.com/problems/find-the-pivot-integer/
Difficulty: Easy
"""

import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        S = n * (n + 1) // 2

        x = int(math.sqrt(S))

        if x * x == S:
            return x
        return -1
