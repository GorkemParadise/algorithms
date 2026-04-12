from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L = sorted(nums1 + nums2)
        n = len(L)
        if n % 2 == 0:
            return float((L[n//2] + L[n//2 - 1]) / 2)
        else:
            return float(L[n//2])
        
sol = Solution
nn = sol.findMedianSortedArrays(None, [1,3], [2])
print(nn)