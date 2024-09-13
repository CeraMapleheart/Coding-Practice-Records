class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        le = len(nums)
        if le%2 ==0:
            n = (nums[le//2]+nums[le//2-1])/2
        else:
            n = (nums[le//2])
        return n