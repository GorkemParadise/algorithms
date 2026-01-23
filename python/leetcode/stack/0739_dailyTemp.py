''' class Solution:
    def dailyTemperatures(self, temperatures):
        ans = []
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(j-i)
                    break
                else:
                    if j == len(temperatures)-1:
                        ans.append(0)
        ans.append(0)
        return ans '''

# Optimized solution using stack

class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)

        return ans

    
sol = Solution()
ss = sol.dailyTemperatures([73,74,75,71,69,72,76,73])
print(ss)

'''
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
'''