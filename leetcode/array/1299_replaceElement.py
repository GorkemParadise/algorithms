class Solution:
    def replaceElements(self, arr):
        out = []
        max = 0
        for i in range(len(arr)):
            for j in range (i + 1, len(arr)):
                if arr[j] > max:
                    max = arr[j]
            if max == 0:
                out.append(-1)
            else:
                out.append(max)
            max = 0
        return out
    
sol = Solution()
print(sol.replaceElements([17,18,5,4,6,1]))  # [18,6,6,6,1,-1]

class Solution:
    def replaceElements2(self, arr):
        n = len(arr)
        max_right = -1

        for i in range(n - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            if current > max_right:
                max_right = current

        return arr

s0l = Solution()
s0l.replaceElements2([17,18,5,4,6,1])  # [18,6,6,6,1,-1]