class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxDist = 0

        for i in range(len(nums)):
            if i > maxDist:
                return False
            maxDist = max(maxDist, i + nums[i])

        return True
