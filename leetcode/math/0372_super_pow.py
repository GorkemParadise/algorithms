"""
Problem: 372. Super Pow
Link: https://leetcode.com/problems/super-pow/
Difficulty: Medium
"""


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:

        MOD = 1337
        
        a %= MOD
        power = 1

        for digit in b:
            power = (pow(power, 10, MOD) * pow(a, digit, MOD)) % MOD

        return power