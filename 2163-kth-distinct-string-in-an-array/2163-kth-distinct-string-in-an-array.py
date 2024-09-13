class Solution(object):
    def kthDistinct(self, arr, k):
        arr1 = []
        for i in arr:
            if arr.count(i) == 1:
                arr1.append(i)
        if len(arr1) < k:
            return ""
        return str(arr1[k-1])

        