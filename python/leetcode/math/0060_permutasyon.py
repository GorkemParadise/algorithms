from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        nums = list(range(1, n+1))
        k -= 1 #index

        result = []

        for i in range(n, 0, -1):
            f = factorial(i-1)
            new_i = k // f

            result.append(str(nums[new_i]))
            nums.pop(new_i)

            k %= f
            
        return ''.join(result)   