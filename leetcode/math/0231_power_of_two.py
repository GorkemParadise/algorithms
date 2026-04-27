"""
Problem: 231. Power of Two
Link: https://leetcode.com/problems/power-of-two/
Difficulty: Easy
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))

''' 
2'nin kuvveti olan sayının örnek bit dizilimi:
1000....0

2'nin kuvveti - 1 olan sayının örnek bit dizilimi:
0111....1

ikisinin ve bağlacında kıyaslanması ile gelen dizilim:
0000....00
'''