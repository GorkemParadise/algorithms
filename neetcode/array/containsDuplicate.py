class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen =[]
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
            else:
                return True
        return False