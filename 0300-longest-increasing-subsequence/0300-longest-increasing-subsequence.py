class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #1 because min 1 length(itself a subsequence) to max of length of nums
        dp = [1] * (len(nums))
        
        #Bottom-up approach -O(n^2)
        #traversing in a reverse order 
        for i in range(len(nums)-1,-1,-1):
            #since it's subsequence, need to check i with all the possible val till start
            for j in range(i+1,len(nums)):
                #below condtion makes sure, it is in increasing order
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
                    
        return max(dp)
                    
        