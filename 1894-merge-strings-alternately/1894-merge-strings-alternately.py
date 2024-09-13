class Solution(object):
    def mergeAlternately(self, word1, word2):
        l1, l2 = len(word1), len(word2)
        i1, i2 = 0, 0
        w = []

        flag = 1
        while i1 < l1 and i2 < l2:
            if flag == 1:
                w.append(word1[i1])
                i1 += 1
                flag = 2
            else:
                w.append(word2[i2])
                i2 += 1
                flag = 1
        while i1 < l1:
            w.append(word1[i1])
            i1 += 1
        while i2 < l2:
            w.append(word2[i2])
            i2 += 1
        return ''.join(w)
            

        



        