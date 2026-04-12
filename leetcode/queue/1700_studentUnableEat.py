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
    