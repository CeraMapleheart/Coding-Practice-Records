class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #if target in nums:
        #    return 1
        l = 0
        min_len = float('inf')
        shortest = 0
        for r in range(len(nums)):
            shortest += nums[r]
            while shortest >= target:
                min_len = min(min_len, r-l+1)
                shortest -= nums[l]
                l += 1        
        return min_len if min_len < float('inf') else 0
        # Time: O(n)
        # Space: O(1)