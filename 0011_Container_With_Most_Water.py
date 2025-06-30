class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1

        maxArea = 0
        while l != r:
            area = (r - l) * min(height[l], height[r])
            if area > maxArea:
                maxArea = area
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxArea
