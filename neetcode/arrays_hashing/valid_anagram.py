"""
Problem: Valid Anagram
Link: https://neetcode.io/problems/is-anagram/question?list=neetcode150
Difficulty: Easy
"""



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        return sorted_s == sorted_t
