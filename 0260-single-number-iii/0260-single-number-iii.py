class Solution(object):
    def singleNumber(self, nums):
        d={}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                del d[i]
        return list(d.keys())
        