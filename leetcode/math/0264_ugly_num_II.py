"""
Problem: 264. Ugly Number II
Link: https://leetcode.com/problems/ugly-number-ii/
Difficulty: Medium
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]

        i2 = i3 = i5 = 0

        for _ in range(1, n):
            next2, next3, next5 = ans[i2] * 2, ans[i3] * 3, ans[i5] * 5
            next_ugly = min(next2, next3, next5)
            ans.append(next_ugly)

            if next_ugly == next2:
                i2 += 1
            if next_ugly == next3:
                i3 += 1
            if next_ugly == next5:
                i5 += 1

        return ans[-1]