class Solution(object):
    def maxDepth(self, s):
        op = [0]
        counter = 0
        for i in s:
            if i in ["(", ")"]:
                if i == "(":
                    counter +=1
                else:
                    op.append(counter)
                    counter -=1
        return max(op)

        