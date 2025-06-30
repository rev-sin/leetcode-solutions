class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        n = len(sequence)
        for i in range(n, 0, -1):
            if i * word in sequence:
                return i

        else:
            return 0
