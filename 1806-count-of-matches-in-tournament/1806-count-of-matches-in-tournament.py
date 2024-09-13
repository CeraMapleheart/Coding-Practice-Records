class Solution(object):
    def numberOfMatches(self, n):
        tot =0
        while n>1:
            tot+= (n//2)
            n= (n//2)+(n%2)
        return tot