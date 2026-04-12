"""
Problem: 1700. Number of Students Unable to Eat Lunch
Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
Difficulty: Easy
"""


from typing import List

# 0: circular
# 1: square
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for s in sandwiches:
            if s not in students:
                break
            students.remove(s)
        return len(students)
    