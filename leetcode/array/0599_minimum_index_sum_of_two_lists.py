"""
Problem: 599. Minimum Index Sum of Two Lists
Link: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
Difficulty: Easy
"""


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        pairs = []

        l1 = len(list1)
        l2 = len(list2)

        if l1 <= l2:
            i = 0
            while i < l1:
                j = 0
                while j < l2:
                    if list1[i] == list2[j]:
                        pairs.append((i + j, list1[i]))
                        break
                    j += 1
                i += 1

        else:
            i = 0
            while i < l2:
                j = 0
                while j < l1:
                    if list2[i] == list1[j]:
                        pairs.append((i + j, list2[i]))
                        break
                    j += 1
                i += 1

        minimum = min(x[0] for x in pairs)

        ans = []

        for s, name in pairs:
            if s == minimum:
                ans.append(name)

        return ans