class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 1):
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                current = nums[i] + nums[l] + nums[r]

                if abs(current - target) < abs(closest - target):
                    closest = current
                
                if current == target:
                    return current
                elif current < target:
                    l += 1
                else:
                    r -= 1
        
        return closest