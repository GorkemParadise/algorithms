from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        stack = []
        prev_time = 0

        for k in logs:
            id, typ, timestamp = k.split(':')
            id, timestamp = int(id), int(timestamp)

            if typ == 'start':
                if stack:
                    times[stack[-1]] += timestamp - prev_time
                stack.append(id)
                prev_time = timestamp
            else:
                times[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        return times


solution = Solution()
mm = solution.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])  # Expected output: [3, 4]
print(mm)