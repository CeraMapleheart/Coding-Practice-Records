class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:(m+n)] = nums2
        nums1.sort()
        return nums1
        