from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
# Sayı işime yarıyorsa Push, yoksa Push ve Pop yap
        for i in range(1, n + 1):
            if len(target) == 0:
                break
            if i == target[0]:
                result.append("Push")
                target.pop(0)
            else:
                result.append("Push")
                result.append("Pop")
        return result
    

sol = Solution()
print(sol.buildArray([1,3], 3))  # ["Push","Push","Pop","Push"]