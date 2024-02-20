class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actualSum = sum(nums)
        expectedSum = n*(n+1)//2
        
        return expectedSum - actualSum
        
        