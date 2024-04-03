class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Selection, bubble and insertion sort are in-place algo
        # Picking Bubble sort
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]

        return nums

        # i = 0
        # j = 0 
        # k = len(nums)-1

        # while (j<=k):
        #     if nums[j] ==0:
        #         nums[i], nums[k] =   nums[k],nums[i]
        #     elif nums[j] == 1:

        