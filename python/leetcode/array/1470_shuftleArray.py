from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1 = nums[:n]
        list2 = nums[n:]
        new_list = []
        for i in range(n):
            new_list.append(list1[i])
            new_list.append(list2[i])
        return new_list
    

sol = Solution()
ss = sol.shuffle([2,5,1,3,4,7], 3)
print(ss)  # Output: [2,3,5,4,1,7]