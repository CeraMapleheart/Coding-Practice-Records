class Solution(object):
    def canBeEqual(self, target, arr):
        return(True if sorted(arr) == sorted(target) else False)