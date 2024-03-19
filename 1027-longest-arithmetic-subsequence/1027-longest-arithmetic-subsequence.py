class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        hashMap = {}
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                diff = nums[j] - nums[i]
                
                hashMap[(j,diff)] = hashMap.get((i,diff),1) + 1
                
        return max(hashMap.values())