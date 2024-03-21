class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsub = nums[0]
        cursum = 0
        for i in nums:
            if cursum<0:
                cursum = 0
            cursum = cursum + i
            maxsub = max(cursum,maxsub)
        return maxsub