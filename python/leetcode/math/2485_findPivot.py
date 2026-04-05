import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        S = n * (n+1) // 2

        x = int(math.sqrt(S))

        if x * x == S:
            return x
        return -1
