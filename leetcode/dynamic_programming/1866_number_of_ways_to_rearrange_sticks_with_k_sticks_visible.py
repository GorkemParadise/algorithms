"""
Problem: 1866. Number of Ways to Rearrange Sticks With K Sticks Visible
Link: https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/
Difficulty: Hard
"""


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = (dp[i-1][j-1] + (i - 1) * dp[i-1][j]) % MOD
        
        return dp[n][k]



#### BRUTE FORCE SOLUTİON - O(N! / (N-K)!) ####
##    class Solution:
  ##      def factorial(self, num):
  ##          if num == 0:
  ##              return 1
  ##          return num * self.factorial(num - 1)
##
  ##      def permute(self, nums):
  ##          if len(nums) == 1:
  ##              return [nums]
##
  ##          result = []
##
  ##          for i in range(len(nums)):
  ##              current = nums[i]
  ##              remaining = nums[:i] + nums[i+1:]
##
  ##              for p in self.permute(remaining):
  ##                  result.append([current] + p)
##
  ##          return result
##
  ##      def rearrangeSticks(self, n: int, k: int) -> int:
  ##          arrays = self.permute(list(range(1, n+1)))
##
  ##          ans = 0
##
  ##          for arr in arrays:
  ##              curr = arr[0]
  ##              count = 1
##
  ##              for j in range(1, n):
  ##                  if arr[j] > curr:
  ##                      curr = arr[j]
  ##                      count += 1
##
  ##              if count == k:
  ##                  ans += 1
##
  ##          return ans