class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        curr_sum = 0
        
        for i in nums:
            if curr_sum < 0:
                curr_sum = 0
                
            curr_sum = i+curr_sum
            res = max(curr_sum,res)
            
        return res