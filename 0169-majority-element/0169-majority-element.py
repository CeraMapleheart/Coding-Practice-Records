class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        num = set(nums)
        for i in num:
            if nums.count(i) > n/2:
                return i        