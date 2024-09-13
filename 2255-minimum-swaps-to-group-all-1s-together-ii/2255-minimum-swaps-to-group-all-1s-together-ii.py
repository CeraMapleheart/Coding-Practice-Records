class Solution(object):
    def minSwaps(self, nums):
        count_ones = nums.count(1)
        if count_ones == 0:
            return 0

        nums_twice = nums + nums

        current_ones = nums_twice[:count_ones].count(1)
        min_swaps = count_ones - current_ones
        
        for i in range(1, len(nums)):
            if nums_twice[i - 1] == 1:
                current_ones -= 1
            if nums_twice[i + count_ones - 1] == 1:
                current_ones += 1
            
            min_swaps = min(min_swaps, count_ones - current_ones)
        
        return min_swaps
