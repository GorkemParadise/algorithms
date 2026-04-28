"""
Problem: Climbing Stairs
Link: https://neetcode.io/problems/climbing-stairs/question?list=neetcode150
Difficulty: Easy
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]    

        return dp[n]
    
        ''' 
        n = 2, output = 2
        n = 3, output = 3
        n = 4, output = 5
        n = 5, output: 8

        1 'ler oluşan ve kendisi total 2
        '''