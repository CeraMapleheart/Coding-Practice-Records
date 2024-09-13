class Solution:
    def minimumPushes(self, word):
        op, counts = 0,[]
        for letter in set(word):
            counts.append(word.count(letter))
        counts.sort(reverse=True)
        for i in range(len(counts)):
            op +=  counts[i] * (i//8 + 1)
        return op