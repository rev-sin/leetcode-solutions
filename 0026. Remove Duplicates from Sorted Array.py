class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1

        for i in nums:
            if i != nums[k - 1]:
                nums[k] = i
                k += 1

        return k
