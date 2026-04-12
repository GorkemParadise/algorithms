"""
Problem: 119. Pascal's Triangle II
Link: https://leetcode.com/problems/pascals-triangle-ii/
Difficulty: Easy
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []

        for i in range(0, rowIndex+1):
            row = [1] * (i + 1)  # i = 2

            for j in range (1, i):  # j = 1
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)

        return result[rowIndex]