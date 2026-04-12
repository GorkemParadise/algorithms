"""
Problem: 1346. Check If N and Its Double Exist
Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/
Difficulty: Easy
"""


class Solution:
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False