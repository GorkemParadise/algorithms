"""
Problem: 728. Self Dividing Numbers
Link: https://leetcode.com/problems/self-dividing-numbers/
Difficulty: Easy
"""


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        
        for num in range(left, right+1):
            state = True
            const = num

            while const > 0:
                digit = const % 10

                if digit == 0 or num % digit != 0:
                    state = False 
                    break

                const //= 10

            if state:
                result.append(num)

        return result
