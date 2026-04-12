"""
Problem: 455. Assign Cookies
Link: https://leetcode.com/problems/assign-cookies/
Difficulty: Easy
"""



class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0 # çocuk
        j = 0 # kurabiye

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i
                