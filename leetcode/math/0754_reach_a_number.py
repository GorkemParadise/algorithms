"""
Problem: 754. Reach a Number
Link: https://leetcode.com/problems/reach-a-number/
Difficulty: Medium
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        # target = 4, output: 3
        # target = 5, output 5
        # target = 6, output 3
        # target = 8, output 4
        target = abs(target)

        s = 0
        total = 0

        while total < target:
            s += 1
            total += s
        
        while (total - target) % 2 != 0:
            s += 1
            total += s
        
        return s