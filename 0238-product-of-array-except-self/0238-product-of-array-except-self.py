class Solution(object):
    def productExceptSelf(self, nums):
        output = [1]*len(nums)
        prefix, suffix = 1,1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i]*suffix
            suffix *= nums[i]
        return output
               