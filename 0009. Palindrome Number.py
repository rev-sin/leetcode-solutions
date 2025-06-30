class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        xrev = strx[::-1]
        if strx == xrev:
            return True

        return False
