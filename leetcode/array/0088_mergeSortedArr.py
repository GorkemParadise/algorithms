class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1

# Example usage:
solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
result = solution.merge(nums1, m, nums2, n)
print(result)  # Output: [1,2,2,3,5,6]