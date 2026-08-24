"""
Problem: 3662. Check Divisibility by Digit Sum and Product
Link: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
Difficulty: Easy
"""


class Solution:
    def checkDivisibility(self, n):
        temp = n
        sum = 0
        product = 1

        while temp > 0:
            sum += temp % 10
            product *= temp % 10
            temp = temp // 10

        total = sum + product

        return total > 0 and n % total == 0
