"""
Problem: 646. Maximum Length of Pair Chain
Link: https://leetcode.com/problems/maximum-length-of-pair-chain/
Difficulty: Medium
"""


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])  # input sorted

        n = len(pairs)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)