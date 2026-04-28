"""
Problem: 1025. Divisor Game
Link: https://leetcode.com/problems/divisor-game/
Difficulty: Easy
"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0