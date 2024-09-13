class Solution(object):
    def longestCommonPrefix(self, strs):
        s = ""
        minimum = min(len(k) for k in strs)
        for i in range (minimum):
            char = strs[0][i]
            for string in strs:
                if char != string[i]:
                    return s
            s = s + strs[0][i]
        return s 