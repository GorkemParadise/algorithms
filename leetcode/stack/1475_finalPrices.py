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