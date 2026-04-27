"""
Problem: 338. Counting Bits
Link: https://leetcode.com/problems/counting-bits/
Difficulty: Easy
"""


from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        s = 1

        for i in range(1, n + 1):
            if s * 2 == i:
                s = i

            ans[i] = ans[i - s] + 1
        
        return ans
            