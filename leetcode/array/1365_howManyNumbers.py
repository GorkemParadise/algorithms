class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        gorulen = 0
        total = []
        for i in range (len(nums)):
            for j in range (len(nums)):
                if nums[i] > nums[j]:
                    gorulen += 1
            total.append(gorulen)
            gorulen = 0
        return total


