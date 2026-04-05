class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0 or k % 5 == 0:
            return -1

        n = 0
        for l in range(1, k + 1):
            n = n * 10 + 1
            if n % k == 0:
                break

        if n % k == 0:
            return l

        return -1
