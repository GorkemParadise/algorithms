"""
Problem: Valid Anagram
Link: https://neetcode.io/problems/valid-anagram
Difficulty: Easy
"""



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        return sorted_s == sorted_t
