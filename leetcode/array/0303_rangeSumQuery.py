class NumArray:

    def __init__(self, nums: List[int]):
        self.now_sum = 0
        self.index = [0]

        for bugra in nums:
            self.now_sum += bugra
            self.index.append(self.now_sum)

    def sumRange(self, left: int, right: int) -> int:
        # index[r + 1], index[l]
        total_right = self.index[right+1]
        total_left = self.index[left]
        
        return total_right - total_left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)