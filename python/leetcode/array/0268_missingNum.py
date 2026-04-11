class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0,1,2,3,4 toplamı: 10, eksik: 5, len = 5
        # 1,2,3,4 toplam: 10, eksik 0, len = 4

        n = len(nums)
        beklenen = n*(n+1)//2
        total = sum(nums)

        return beklenen - total