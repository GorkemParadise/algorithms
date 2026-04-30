"""
Problem: 1137. N-th Tribonacci Number
Link: https://leetcode.com/problems/n-th-tribonacci-number
Difficulty: Easy
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        # T0 = 0
        # T1 = 1
        # T2 = 1
        # T3 = 2
        # T4 = 4
        # T5 = 7
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]