"""
Problem: 1475. Final Prices With a Special Discount in a Shop
Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
Difficulty: Easy
"""


from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break

        return prices   


sol = Solution()
l = sol.finalPrices([8,4,6,2,3])
print(l)  # [4,2,4,2,3]