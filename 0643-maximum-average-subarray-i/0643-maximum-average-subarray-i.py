class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        right = k
        final = float(sum(nums[left:right]))
        currentSum = final
        while right < len(nums):
            currentSum = currentSum - nums[left] + nums[right]
            if currentSum > final:
                final = currentSum
            left += 1
            right += 1
        return final/k