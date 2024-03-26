class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #O(n*2^n)T
        #result array initialized
        result = []

        #subset array is temporary array generated different subset
        subset = []

        #recursion function
        def backtrack(index):

            #Base case
            if index>= len(nums):
                result.append(subset.copy())
                return

            #decision to TAKE the value
            subset.append(nums[index])
            backtrack(index+1)

            #decision to NOT TAKE the value
            subset.pop()
            backtrack(index+1)


        backtrack(0)
        return result

        