"""
Problem: 191. Number of 1 Bits
Link: https://leetcode.com/problems/number-of-1-bits/
Difficulty: Easy
"""


from typing import List
import math


class Solution:
    def hammingWeight(self, n: int) -> int:
        t = int(math.log(n, 2)) + 1
        dp = [0] * t

        i = t - 1

        while i >= 0:
            if n % 2 == 1:
                dp[i] = 1
            n = n // 2
            i = i - 1

        return sum(dp)