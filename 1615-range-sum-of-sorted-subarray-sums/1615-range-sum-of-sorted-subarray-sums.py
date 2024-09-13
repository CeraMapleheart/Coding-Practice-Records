class Solution(object):
    def rangeSum(self, nums, n, left, right):
        arr = []
        for i in range(0,len(nums)):
            counter = 0
            for j in range (i, len(nums)):
                counter += nums[j]
                arr.append(counter)
        arr.sort()
        mod = (10**9 + 7)
        return sum(arr[left-1:right])%mod
        