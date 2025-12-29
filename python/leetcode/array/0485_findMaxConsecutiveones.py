def findMaxConsecutiveOnes(self, nums):
    total = 0
    answer = []
    for i in nums:
        if i == 1:
            total += 1
        else:
            answer.append(total)
            total = 0
    answer.append(total)
    return max(answer)

# Example usage:
nums = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(None, nums))  # Output: 3