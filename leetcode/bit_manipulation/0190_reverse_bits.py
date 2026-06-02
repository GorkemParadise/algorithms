"""
Problem: 190. Reverse Bits
Link: https://leetcode.com/problems/reverse-bits/
Difficulty: Easy
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        # 5 : 0101 --> 1010: 10
        # 7 : 0111 --> 1110: 16
        # 8 : 1000 --> 0001: 1
        r = 0
        for bit in range(32):
            r *= 2
            r += n % 2
            n //= 2
        return r