class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        for i in range(max(len(word1), len(word2))):
            try:
                res += word1[i]
            except:
                pass
            try:
                res += word2[i]
            except:
                pass

        return res
