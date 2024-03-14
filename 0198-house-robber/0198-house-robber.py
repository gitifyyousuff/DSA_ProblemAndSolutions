class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #bottom-up approach - O(n)TS
#         n = len(nums)
#         if n == 1:
#             return nums[0]
        
#         running_max = [nums[0],max(nums[0],nums[1])]
        
#         for i in range(2,n):
#             curr_val = max(nums[i]+running_max[i-2],running_max[i-1])
#             running_max.append(curr_val)
            
#         return running_max[-1]

        #O(n)T,O(1)S
        loot1,loot2 = 0,0
        
        for v in nums:
            temp = max(loot1+v,loot2)
            loot1 = loot2
            loot2 = temp
            
        return loot2
    