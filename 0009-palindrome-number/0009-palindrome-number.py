class Solution(object):
    def isPalindrome(self, x):
        n=str(x)
        l, r=0, len(n)-1
        while l<r:
            if n[l] == n[r]:
                l+=1
                r-=1
            else:
                return False
        return True