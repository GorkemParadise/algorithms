"""
Problem: 349. Intersection of Two Arrays
Link: https://leetcode.com/problems/intersection-of-two-arrays/
Difficulty: Easy
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        intersec = []
        n1 = len(nums1)
        n2 = len(nums2)

        for i in range(n1):
            for j in range(n2):

                if nums1[i] == nums2[j]:
                    if nums1[i] not in intersec:

                        intersec.append(nums1[i])
                    break

        return intersec