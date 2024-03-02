class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #O(n)T 
        #2 pointer technique
        res = 0
        l,r =0,len(height)-1

        while l<r:
            #calculating area 
            #taking min height because water overflow may happen if max taken 
            area = (r-l)*min(height[l],height[r])
            res = max(res,area)
            #if the height of right pointer (right side) is max, then we 
            #need to increment left pointer to get better value to find water area
            #if equal any pointer can be shifted
            #if height of left pointer is max, shift right to decrement
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
