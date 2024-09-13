class Solution(object):
    def removeElement(self, nums, val):
        n = nums.count(val)
        for i in range (0, n):
            nums.remove(val) 
        print nums
        