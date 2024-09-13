class Solution(object):
    def isSubsequence(self, s, t):
        p1, p2 = 0, 0
        while p2 < len(t) and p1 < len(s):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        if p1 == len(s): return True
        else: return False
        