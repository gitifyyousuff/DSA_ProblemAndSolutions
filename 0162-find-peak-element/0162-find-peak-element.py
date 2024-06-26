class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left  = 0
        right = len(nums)-1

        while left<=right-1:
            mid = (left+right)//2

            if nums[mid]> nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid

            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        return left if nums[left]>=nums[right] else right

            

