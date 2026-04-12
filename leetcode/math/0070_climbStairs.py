from typing import List

'''
n = 3, output = 3
1 + 1 + 1
1 + 2
2 + 1


n = 4, output = 5
1 + 1 + 1 + 1
1 + 2 + 1
2 + 1 + 1
1 + 1 + 2
2 + 2

n = 5, output = 8
1 + 1 + 1 + 1 + 1
1 + 2 + 2
2 + 1 + 2
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 2 + 1
1 + 1 + 1 + 2
1 + 2 + 1 + 1

n = 6, output = 13
1 + 1 + 1 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1 (5)
2 + 2 + 1 + 1 (6)
2 + 2 + 2


'''
# math kullanmadan ve dp kullanmadan çözülecek

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b

        return b