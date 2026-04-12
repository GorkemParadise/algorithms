"""
Problem: 120. Triangle
Link: https://leetcode.com/problems/triangle/
Difficulty: Medium
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        S = len(triangle) # [[2],[3,4],[6,5,7],[4,1,8,3]] , S = 4
        
        ters = triangle[-1]  # [[4,1,8,3], [6,5,7], [3,4], [2]]

        for i in range(S - 2, -1, -1):  # -1 0 1 2
            for j in range(len(triangle[i])): # 0 1 2 3
                ters[j] = triangle[i][j] + min(ters[j], ters[j+1])

        return ters[0]
