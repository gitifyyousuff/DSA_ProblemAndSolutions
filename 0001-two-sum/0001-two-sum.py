class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash={}
        for i in range(len(nums)):
            pm = target-nums[i]
            if pm in num_hash:
                return[i,num_hash[pm]]
            else:
                num_hash[nums[i]]= i
                
        return []