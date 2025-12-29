class Solution:
    def validMountainArray(self,arr):
        n = len(arr)
        if n < 3:
            return False

        k = arr.index(max(arr))
        if k == 0 or k == n - 1:
            return False
        
        for i in range(1, k + 1):
            if arr[i] <= arr[i - 1]:
                return False
        for i in range(k + 1, n):
            if arr[i] >= arr[i - 1]:
                return False
        return True

# Example usage:
sol = Solution()
print(sol.validMountainArray([2, 1]))  # Output: False
print(sol.validMountainArray([3, 5, 5]))  # Output: False
print(sol.validMountainArray([0, 3, 2, 1]))  # Output: True