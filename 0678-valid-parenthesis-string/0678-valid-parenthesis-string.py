class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmin = 0
        cmax = 0

        for i in s:
            if i == "(":
                cmin+=1
                cmax+=1

            elif i == ")":
                cmin-=1
                cmax-=1

            else:
                cmin-=1
                cmax+=1

            # Extra right parenthessis
            if cmax < 0:
                return False
                
            if cmin < 0:
                cmin = 0

        return cmin == 0