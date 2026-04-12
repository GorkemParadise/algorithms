"""
Problem: 202. Happy Number
Link: https://leetcode.com/problems/happy-number/
Difficulty: Easy
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        
        def find_digits(n):
            digits = []
            while n > 0:
                digits.append(n % 10)
                n = n // 10
            return digits

        def square(digits):
            for i in range(len(digits)):
                digits[i] = digits[i] ** 2
            return digits

        def sol(n, seen):
            if n == 1:
                return True
            if n in seen:
                return False

            seen.add(n)
            digits = find_digits(n)
            squared = square(digits)
            new_n = sum(squared)

            return sol(new_n, seen)
            
        return sol(n, set())