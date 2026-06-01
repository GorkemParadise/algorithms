"""
Problem: 1922. Count Good Numbers
Link: https://leetcode.com/problems/count-good-numbers/
Difficulty: Medium
"""


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        # 0 1 2 3 4 5 6 7 8  --> 9 index, 9 num
        # 5 even
        # 4 odd

        even = (n + 1) // 2  
        odd  = n // 2       
        
        return pow(5, even, MOD) * pow(4, odd, MOD) % MOD

