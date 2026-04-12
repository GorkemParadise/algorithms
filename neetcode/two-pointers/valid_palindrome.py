"""
Problem: Valid Palindrome
Link: https://neetcode.io/problems/is-palindrome/question?list=neetcode150
Difficulty: Easy
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = s.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace('"', "").replace(":", "").replace(";", "").replace("-", "").replace("_", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("/", "").replace("\\", "").replace("|", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("+", "").replace("=", "").replace("<", "").replace(">", "").replace("~", "").replace("`", "").replace(" ", "")

        return ss == ss[::-1]
    


# ALTERNATIVE SOLUTION

class Solution:
    def Palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True