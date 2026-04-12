from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = len(tickets)
        time = 0
        while tickets[k] > 0:
            for i in range(t):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
                if tickets[k] == 0:
                    break
        return time
    