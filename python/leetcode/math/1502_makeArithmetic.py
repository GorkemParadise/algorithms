from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        fark = arr[1] - arr[0] # 3

        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != fark:
                return False
        return True


        # 2, 5, 8, 11, 14, 17, 20
        # 7 elemeanlı

