from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set()
        situation = True
        duplicate = -1
        for num in nums:
            if num in num_set:
                duplicate = num
                situation = False
            else:
                num_set.add(num)
        if situation:
            return [-1, -1]
        for i in range(1, n + 1):
            if i not in num_set:
                return [duplicate, i]
        return [-1, -1]